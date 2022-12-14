
"""Run a cross platform testing with some configurations.

It should be run via script with the following command:
OPTION A:
To generate new programs and execute them:
cross_platform_testing.py generate --config_file=config.yaml

OPTION B:
To run a detector/statistical test on the produced bitstrings:
cross_platform_testing.py detect --config_file=config.yaml

Note: insert the tag --benchmark to run only the benchmark configurations
as specified by the is_benchmark flag in the congig.yaml file.


"""


import click
import os
from utils import iterate_parallel, load_config_and_check
from utils import iterate_parallel_n
from utils import iterate_over
from pathlib import Path
import shutil
import random

from typing import Any, Dict
from generation_strategy import *
import subprocess
import sys
import json

from itertools import combinations

from detectors import *
from generation_strategy import *
from simulators import *
from simulators_mockup import *
from utils import convert
from utils import run_programs
from utils import iterate_over_program_ids
from utils import iterate_over_pairs_of_group
import time


def replace_in_all_files(folder, detect_string, substitute_string):
    """Replace the given string in all the files in the folder."""
    for circuit_id, content in iterate_over(folder, filetype=".py", parse_json=False):
        content = content.replace(detect_string, substitute_string)
        with open(os.path.join(folder, circuit_id + ".py"), "w") as f:
            f.write(content)
            f.close()



def get_folder(config, comparison_name, stage, compiler_name=None):
    if compiler_name is None:
        return os.path.join(
            config["experiment_folder"], comparison_name, stage)
    return os.path.join(
        config["experiment_folder"], comparison_name, stage, compiler_name)


def prepare_folders(config: Dict[str, Any], benchmark_mode: bool) -> None:
    """Prepare the folders."""
    click.echo("Checking folder structure...")
    comparisons = config["comparisons"]
    experiment_folder = config["experiment_folder"]
    Path(experiment_folder).mkdir(parents=True, exist_ok=True)
    for comparison in comparisons:
        if benchmark_mode and not comparison.get("is_benchmark", False):
            print("Skipping folder creation: ", comparison["name"])
            print("[Not part of the benchmark.]")
            continue
        comparison_name = comparison["name"]
        compilers = comparison["compilers"]
        subfolder = os.path.join(experiment_folder, comparison_name)
        Path(subfolder).mkdir(parents=True, exist_ok=True)
        for stage_folder in ["programs", "executions", "ground_truth", "predictions"]:
            Path(os.path.join(subfolder, stage_folder)).mkdir(
                parents=True, exist_ok=True)
            if stage_folder in ["programs", "executions"]:
                for compiler in compilers:
                    Path(os.path.join(subfolder, stage_folder, compiler["name"])).mkdir(
                        parents=True, exist_ok=True)
        Path(os.path.join(subfolder, "original_programs")).mkdir(
                        parents=True, exist_ok=True)
    click.echo("Folder structure checked and ready.")


def get_compiler(role: str, comparison_config: Dict[str, Any]):
    """Reconstruct and return the compiler for master or slave."""
    lookup_compiler = [
        c for c in comparison_config["compilers"]
        if c["benchmark_role"] == role][0]
    return lookup_compiler


def get_generator_name(role: str, comparison_config: Dict[str, Any]):
    """Reconstruct and return the generator name for master or slave."""
    lookup_compiler = get_compiler(role, comparison_config)
    return lookup_compiler['name']


def get_generator_folder(role: str, comparison_config: Dict[str, Any], config: Dict[str, Any]):
    """Reconstruct and return the generator folder for master or slave."""
    lookup_compiler = get_compiler(role, comparison_config)
    return get_folder(
        config, comparison_config["name"], "programs", lookup_compiler["name"])


def get_generator(role: str, comparison_config: Dict[str, Any], config: Dict[str, Any]):
    """Reconstruct and return the generator for master or slave."""
    lookup_compiler = get_compiler(role, comparison_config)
    if 'generation_object' in lookup_compiler.keys():
        generator_name = lookup_compiler['generation_object']
    else:
        generator_name = comparison_config['generation_object']
    return eval(generator_name)(
        out_folder=get_generator_folder(role, comparison_config, config),
        benchmark_name=comparison_config["name"]
    )


def generate_together(
        comparison_config: Dict[str, Any], config: Dict[str, Any]):
    """Jointly generate the samples "master" and "slave" in a sequential way.

    Note that we need this generation to propagate the number of qubits that
    are generated by the two possibly different generators, since we want
    circuit with at least the same output, which makes them comparable.
    """
    click.echo("Joint generation...")
    n_generated_programs = config["n_generated_programs"]
    random.seed(config["random_seed"])
    stop_generation = False
    for i in range(n_generated_programs):
        # sample a number of qubits
        n_qubits = random.randint(config["min_n_qubits"], config["max_n_qubits"])
        # create the program and store them automatically
        for role in ["master", "slave"]:
            generator = get_generator(role=role,
                comparison_config=comparison_config, config=config)
            experiment_level_seed = config["random_seed"]
            lookup_compiler = get_compiler(role, comparison_config)
            seed = lookup_compiler.get("random_seed", experiment_level_seed)
            try:
                generator.generate(
                    n_qubits=n_qubits,
                    n_ops_range=(config["min_n_ops"], config["max_n_ops"]),
                    gate_set=config["gate_set"],
                    random_seed=seed,
                    circuit_id=str(i))
            except NoMoreProgramsAvailable:
                stop_generation = True
        if stop_generation:
            break


def generate_once_and_copy(
        comparison_config: Dict[str, Any], config: Dict[str, Any]):
    """Generate the samples "master" and copy the same in sample "slave"."""
    click.echo("Generate Once&Copy generation...")
    n_generated_programs = config["n_generated_programs"]
    source_folder = get_generator_folder(
        role="master", comparison_config=comparison_config, config=config)
    generator = eval(comparison_config['generation_object'])(
        out_folder=source_folder,
        benchmark_name=comparison_config["name"]
    )
    random.seed(config["random_seed"])
    for i in range(n_generated_programs):
        # sample a number of qubits
        n_qubits = random.randint(config["min_n_qubits"], config["max_n_qubits"])
        # create the program and store them automatically
        try:
            generator.generate(
                n_qubits=n_qubits,
                n_ops_range=(config["min_n_ops"], config["max_n_ops"]),
                gate_set=config["gate_set"],
                random_seed=config["random_seed"],
                circuit_id=str(i))
        except NoMoreProgramsAvailable:
            break
    dest_folder = get_generator_folder(
        role="slave", comparison_config=comparison_config, config=config)
    # copy the files
    for file in os.listdir(source_folder):
        shutil.copy(os.path.join(source_folder, file), dest_folder)


def generate_once_and_derive(
        comparison_config: Dict[str, Any], config: Dict[str, Any]):
    """Generate the samples for "master" and derive in "slave" samples"""
    click.echo("Generate Once&Derive generation...")
    n_generated_programs = config["n_generated_programs"]

    # load the generator objects for the two samples
    generator_master = get_generator(
        role="master", comparison_config=comparison_config, config=config)

    generator_slave = get_generator(
        role="slave", comparison_config=comparison_config, config=config)

    random.seed(config["random_seed"])
    stop_generation = False
    for i in range(n_generated_programs):
        # sample a number of qubits
        n_qubits = random.randint(config["min_n_qubits"], config["max_n_qubits"])
        # create the program and store them automatically
        try:
            qasm_content, metadata = generator_master.generate(
                n_qubits=n_qubits,
                n_ops_range=(config["min_n_ops"], config["max_n_ops"]),
                gate_set=config["gate_set"],
                random_seed=config["random_seed"],
                circuit_id=str(i))
        except NoMoreProgramsAvailable:
            stop_generation = True

        # derive the B sample
        generator_slave.load_existing_program(qasm_content, metadata)
        try:
            qasm_content, metadata = generator_slave.generate(
                n_qubits=n_qubits,
                n_ops_range=(config["min_n_ops"], config["max_n_ops"]),
                gate_set=config["gate_set"],
                random_seed=config["random_seed"],
                circuit_id=str(i))
        except NoMoreProgramsAvailable:
            stop_generation = True

        if stop_generation:
            break


def execute_single_compiler(compiler: Dict[str, Any], comparison_config: Dict[str, Any], config: Dict[str, Any]):
    """Execute the programs of the given compiler."""
    click.echo("Joint execution...")
    n_shots = config["fixed_sample_size"]
    program_folder = get_folder(
        config, comparison_config["name"], "programs", compiler["name"])
    exec_folder = get_folder(
        config, comparison_config["name"], "executions", compiler["name"])
    executor = eval(compiler["execution_object"])(repetitions=n_shots)
    for circuit_id, qasm_content in iterate_over(program_folder, ".qasm"):
        for exec_iteration in range(int(config["n_executions"])):
            # load the program
            executor.from_qasm(qasm_content)
            # execute the program
            executor.execute(n_shots)
            result = executor.get_result()
            with open(os.path.join(exec_folder, f"{circuit_id}_{exec_iteration}.json"), "w") as execution_file:
                print(f"Saving execution of: {circuit_id}.json")
                json.dump(result, execution_file)


def generate_and_run_programs(config: Dict[str, Any], benchmark_mode: bool=False) -> None:
    """Generate and run the programs."""

    prepare_folders(config, benchmark_mode)

    # PSEUDO CODE

    # if we have two compiler-level generator, use them
    # > "programs/compiler_name_1"
    # > "programs/compiler_name_2"

    # otherwise a single comparison-level generator > "original_programs"

    # the execution object is always specified at compiler-level

    for comparison in config["comparisons"]:

        if comparison.get("is_benchmark", False) != benchmark_mode:
            print("Skipping comparison: ", comparison["name"])
            if benchmark_mode:
                print("[Not part of the benchmark.]")
            continue

        # GENERATE QASM PROGRAMS
        # some compilers (fake ones) might have their own generation strategy,
        # such as the random generator, or the case where the programs
        # are derived by the original programs appending a not.
        master_slave_relationship = comparison["master_slave_relationship"]

        # sample generation
        if master_slave_relationship == "identical":
            generate_once_and_copy(comparison_config=comparison, config=config)
        elif master_slave_relationship == "independent":
            generate_together(comparison_config=comparison, config=config)
        elif master_slave_relationship == "derive_slave_from_master":
            generate_once_and_derive(comparison_config=comparison, config=config)

        # GENERATE GROUND TRUTH
        # ground truth must be generated after the creation of the programs
        # because we do not know if all the programs we wanted to generate
        # have been created.
        # We use only one compiler because at this point both the master and
        # the slave will have the same file names to create the ground truths.
        if benchmark_mode and \
                "expected_divergence" in comparison.keys():
            print("Creating ground truth based on expected divergence:",
                  comparison["name"])
            lookup_compiler = get_compiler(
                role="master", comparison_config=comparison)
            ground_truth_folder = get_folder(
                config, comparison["name"], "ground_truth")
            record = {"expected_divergence": comparison["expected_divergence"]}
            # create ground truth
            # based on the number of generated programs in the QASM folder
            generated_qasms_filenames = [
                f.replace(".qasm", "") for f in os.listdir(get_folder(
                    config, comparison["name"], "programs", lookup_compiler["name"]))
                if f.endswith(".qasm")
            ]
            for i in generated_qasms_filenames:
                # save json file with record
                record["circuit_id"] = str(i)
                record["benchmark_name"] = comparison["name"]
                with open(os.path.join(ground_truth_folder, f"{i}.json"), "w") as f:
                    json.dump(record, f)

        # EXECUTE PROGRAMS

        # for those which require qconvert create the .py files first
        for compiler in comparison["compilers"]:

            if compiler.get("execution_object") == "qconvert":
                compiler_specific_folder = get_folder(
                    config, comparison["name"], "programs", compiler["name"])
                convert(
                    source_folder=compiler_specific_folder,
                    dest_folder=compiler_specific_folder,
                    dest_format=compiler["platform"],
                    qconvert_path=config["qconvert_path"])
                # the number of shots are available at experiment-level
                # in the field "platform_dependent_settings"
                current_compiler_settings = [
                    setting for setting in config["platform_dependent_settings"]
                    if setting["platform"] == compiler["platform"]][0]
                shots_lookup = current_compiler_settings.get("shots_lookup")
                shots_substitute = current_compiler_settings.get("shots_substitute")
                replace_in_all_files(
                    folder=compiler_specific_folder,
                    detect_string=shots_lookup,
                    substitute_string=shots_substitute.format(
                        injected_shot=config["fixed_sample_size"]))
                run_programs(
                    source_folder=compiler_specific_folder,
                    dest_folder=get_folder(
                            config, comparison["name"], "executions", compiler["name"]),
                    python_path=config["python_path"],
                    n_executions=config["n_executions"])
            elif compiler.get("execution_object") != "qconvert":
                execute_single_compiler(
                    compiler=compiler,
                    comparison_config=comparison,
                    config=config)


def detect_divergence(config: Dict[str, Any], benchmark_mode: bool = False) -> None:
    """Detect the divergence."""

    detectors = config["detectors"]

    for detector in detectors:
        print("-" * 80)
        print("Running detector:", detector["name"])
        detector_object = eval(detector["detector_object"])()
        for comparison in config["comparisons"]:

            if comparison.get("is_benchmark", False) != benchmark_mode:
                print("Skipping detection: ", comparison["name"])
                if benchmark_mode:
                    print("[Not part of the benchmark.]")
                continue

            compiler_names = [
                compiler["name"] for compiler in comparison["compilers"]]

            random_seed = detector.get("random_seed", None)

            for program_id, group_same_program_id in iterate_over_program_ids(
                    execution_folder=get_folder(
                        config, comparison["name"], "executions"),
                    compilers_names=compiler_names):
                print("Circuit ID: ", program_id)
                print("-" * 80)
                # print("Elements in the group:", group_same_program_id)
                # print("-" * 80)

                # generate program-specific json output
                prediction = {
                    "test": detector["name"],
                    "test_long_name": detector["test_long_name"],
                    "comparison_name": comparison["name"],
                    "circuit_id": program_id,
                    "random_seed": random_seed
                }
                comparisons = []

                for path_exec_a, path_exec_b, res_A, res_B in iterate_over_pairs_of_group(group_same_program_id):
                    # print("res_a: ", len(res_A))
                    # print("res_b: ", len(res_B))
                    sorted_paths = sorted([path_exec_a, path_exec_b])
                    # ran detector

                    pair = {
                        "platform_a": sorted_paths[0].split("/")[-2],
                        "platform_b": sorted_paths[1].split("/")[-2],
                        "path_exec_a": sorted_paths[0],
                        "path_exec_b": sorted_paths[1]
                    }

                    try:
                        start_time = time.time()
                        statistic, p_value = detector_object.check(res_A, res_B, random_seed)
                        pair[f"time"] = time.time() - start_time
                        pair[f"statistic"] = statistic
                        pair[f"statistic"] = statistic
                        pair[f"p_value"] = p_value
                    except Exception as e:
                        pair[f"time"] = -1
                        prediction[f"statistic"] = 0
                        pair[f"p_value"] = -1
                        pair["exception"] = str(e)

                    comparisons.append(pair)

                # save detector result for this program_ID
                prediction["comparisons"] = comparisons

                # save file
                detector_pred_folder = get_folder(
                    config, comparison["name"], "predictions", detector["name"])
                Path(detector_pred_folder).mkdir(parents=True, exist_ok=True)
                with open(os.path.join(detector_pred_folder, program_id + ".json"), "w") as file:
                    json.dump(prediction, file)
                    file.close()


@click.group()
def cli():
    pass


@cli.command()
@click.argument('config_file')
@click.option('--benchmark', is_flag=True)
def generate(config_file, benchmark):
    config = load_config_and_check(config_file, [
        "min_n_qubits",
        "max_n_qubits",
        "n_generated_programs",
        "fixed_sample_size"
        ])

    click.echo('Generate and Run Programs')
    generate_and_run_programs(config, benchmark)


@cli.command()
@click.argument('config_file')
@click.option('--benchmark', is_flag=True)
def detect(config_file, benchmark):
    config = load_config_and_check(config_file, [
        "detectors"
        ])
    click.echo('Detect Divergence')
    detect_divergence(config, benchmark)


if __name__ == '__main__':
    cli()

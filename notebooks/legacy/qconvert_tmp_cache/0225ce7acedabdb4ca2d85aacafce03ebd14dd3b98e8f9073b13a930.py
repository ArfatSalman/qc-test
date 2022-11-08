import cirq
import numpy as np
from functools import reduce

q = [cirq.NamedQubit('q' + str(i)) for i in range(14)]

circuit = cirq.Circuit(
    cirq.rx(2.5009858166994063)(q[0]),
    cirq.ry(5.562672506903891)(q[1]),
    cirq.rz(1.1023958963447806)(q[2]),
    cirq.rz(1.220338852225453)(q[3]),
    cirq.ry(1.4253497199469332)(q[4]),
    cirq.rx(2.6584562936267786)(q[10]),
    cirq.CNOT(q[12], q[13]),
    cirq.rx(6.209957416856063)(q[0]),
    cirq.CNOT(q[4], q[10]),
    cirq.rz(2.2731851653103794)(q[4]),
    cirq.rx(3.986058781630306)(q[7]),
    cirq.rz(3.839173944630678)(q[10]),
    cirq.CNOT(q[4], q[9]),
    cirq.CNOT(q[6], q[5]),
    cirq.rx(0.7264518012019154)(q[8]),
    cirq.rx(1.9619951281825225)(q[5]),
    cirq.CNOT(q[5], q[12]),
    cirq.CNOT(q[6], q[13]),
    cirq.CNOT(q[4], q[6]),
    cirq.ry(0.9987729005246175)(q[7]),
    cirq.rx(0.757932261775076)(q[8]),
    cirq.ry(0.10134279452259236)(q[10]),
    cirq.ry(0.5227295283213563)(q[11]),
    cirq.ry(3.2070781312980996)(q[12]),
    cirq.ry(2.236279054882737)(q[13]),
    cirq.rz(3.42476328964376)(q[8]),
    cirq.ry(3.4762184199159)(q[11]),
    cirq.rx(6.180335123765394)(q[12]),
    cirq.ry(3.926384502772141)(q[8]),
    cirq.ry(6.179648524241403)(q[12]),
    cirq.CNOT(q[9], q[4]),
    cirq.CNOT(q[4], q[6]),
    cirq.ry(2.4438485325496067)(q[7]),
    cirq.rz(4.346090578542644)(q[8]),
    cirq.CNOT(q[5], q[3]),
    cirq.CNOT(q[7], q[9]),
    cirq.CNOT(q[1], q[5]),
    cirq.rz(1.990437060666522)(q[5]),
    cirq.CNOT(q[2], q[11]),
    cirq.CNOT(q[7], q[8]),
    cirq.CNOT(q[7], q[11]),
    cirq.CNOT(q[10], q[2]),
    cirq.measure(q[0], key='c0'),
    cirq.measure(q[1], key='c1'),
    cirq.measure(q[2], key='c2'),
    cirq.measure(q[3], key='c3'),
    cirq.measure(q[4], key='c4'),
    cirq.measure(q[5], key='c5'),
    cirq.measure(q[6], key='c6'),
    cirq.measure(q[7], key='c7'),
    cirq.measure(q[8], key='c8'),
    cirq.measure(q[9], key='c9'),
    cirq.measure(q[10], key='c10'),
    cirq.measure(q[11], key='c11'),
    cirq.measure(q[12], key='c12'),
    cirq.measure(q[13], key='c13')
)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=8192)
result_dict = dict(result.multi_measurement_histogram(keys=['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
print(counts)
from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute, Aer
import numpy as np

shots = 8192

qc = QuantumCircuit()

q = QuantumRegister(8, 'q')
ans = ClassicalRegister(8, 'ans')

qc.add_register(q)
qc.add_register(ans)

qc.rx(np.pi * 0.3501408748, q[0])
qc.rx(np.pi * 0.3501408748, q[1])
qc.rx(np.pi * 0.3501408748, q[2])
qc.rx(np.pi * 0.3501408748, q[3])
qc.rx(np.pi * 0.3501408748, q[4])
qc.rx(np.pi * 0.3501408748, q[5])
qc.rx(np.pi * 0.3501408748, q[6])
qc.rx(np.pi * 0.3501408748, q[7])
qc.ry(np.pi * 0.3501408748, q[0])
qc.ry(np.pi * 0.3501408748, q[1])
qc.ry(np.pi * 0.3501408748, q[2])
qc.ry(np.pi * 0.3501408748, q[3])
qc.ry(np.pi * 0.3501408748, q[4])
qc.ry(np.pi * 0.3501408748, q[5])
qc.ry(np.pi * 0.3501408748, q[6])
qc.ry(np.pi * 0.3501408748, q[7])
qc.rz(np.pi * 0.3501408748, q[0])
qc.rz(np.pi * 0.3501408748, q[1])
qc.rz(np.pi * 0.3501408748, q[2])
qc.rz(np.pi * 0.3501408748, q[3])
qc.rz(np.pi * 0.3501408748, q[4])
qc.rz(np.pi * 0.3501408748, q[5])
qc.rz(np.pi * 0.3501408748, q[6])
qc.rz(np.pi * 0.3501408748, q[7])
qc.rz(np.pi * 1.1, q[0])
qc.rz(np.pi * 1.1, q[1])
qc.rz(np.pi * 1.1, q[2])
qc.rz(np.pi * 1.1, q[3])
qc.rz(np.pi * 1.1, q[4])
qc.rz(np.pi * 1.1, q[5])
qc.rz(np.pi * 1.1, q[6])
qc.rz(np.pi * 1.1, q[7])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[0])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[1])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[2])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[3])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[4])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[5])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[6])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[7])
qc.rx(np.pi * 0.5, q[0])
qc.rx(np.pi * 0.5, q[2])
qc.rx(np.pi * 0.5, q[4])
qc.rx(np.pi * 0.5, q[6])
qc.cx(q[0], q[1])
qc.cx(q[2], q[3])
qc.cx(q[4], q[5])
qc.cx(q[6], q[7])
qc.rx(np.pi * 0.4, q[0])
qc.ry(np.pi * 0.5, q[1])
qc.rx(np.pi * 0.4, q[2])
qc.ry(np.pi * 0.5, q[3])
qc.rx(np.pi * 0.4, q[4])
qc.ry(np.pi * 0.5, q[5])
qc.rx(np.pi * 0.4, q[6])
qc.ry(np.pi * 0.5, q[7])
qc.cx(q[1], q[0])
qc.cx(q[3], q[2])
qc.cx(q[5], q[4])
qc.cx(q[7], q[6])
qc.rx(np.pi * -0.5, q[1])
qc.rx(np.pi * -0.5, q[3])
qc.rx(np.pi * -0.5, q[5])
qc.rx(np.pi * -0.5, q[7])
qc.rz(np.pi * 0.5, q[1])
qc.rz(np.pi * 0.5, q[3])
qc.rz(np.pi * 0.5, q[5])
qc.rz(np.pi * 0.5, q[7])
qc.cx(q[0], q[1])
qc.cx(q[2], q[3])
qc.cx(q[4], q[5])
qc.cx(q[6], q[7])
qc.u3(np.pi * 0.5, np.pi * 0.65, np.pi * 1, q[0])
qc.u3(np.pi * 0.5, np.pi * 0.15, 0, q[1])
qc.u3(np.pi * 0.5, np.pi * 0.65, np.pi * 1, q[2])
qc.u3(np.pi * 0.5, np.pi * 0.15, 0, q[3])
qc.u3(np.pi * 0.5, np.pi * 0.65, np.pi * 1, q[4])
qc.u3(np.pi * 0.5, np.pi * 0.15, 0, q[5])
qc.u3(np.pi * 0.5, np.pi * 0.65, np.pi * 1, q[6])
qc.u3(np.pi * 0.5, np.pi * 0.15, 0, q[7])
qc.u3(0, np.pi * 1, np.pi * 0.5, q[0])
qc.u3(0, 0, np.pi * 0.5, q[1])
qc.u3(0, np.pi * 1, np.pi * 0.5, q[2])
qc.u3(0, 0, np.pi * 0.5, q[3])
qc.u3(0, np.pi * 1, np.pi * 0.5, q[4])
qc.u3(0, 0, np.pi * 0.5, q[5])
qc.u3(0, np.pi * 1, np.pi * 0.5, q[6])
qc.u3(0, 0, np.pi * 0.5, q[7])
qc.rx(np.pi * 0.5, q[0])
qc.rx(np.pi * 0.5, q[2])
qc.rx(np.pi * 0.5, q[4])
qc.rx(np.pi * 0.5, q[6])
qc.cx(q[0], q[1])
qc.cx(q[2], q[3])
qc.cx(q[4], q[5])
qc.cx(q[6], q[7])
qc.rx(np.pi * 0.4, q[0])
qc.ry(np.pi * 0.5, q[1])
qc.rx(np.pi * 0.4, q[2])
qc.ry(np.pi * 0.5, q[3])
qc.rx(np.pi * 0.4, q[4])
qc.ry(np.pi * 0.5, q[5])
qc.rx(np.pi * 0.4, q[6])
qc.ry(np.pi * 0.5, q[7])
qc.cx(q[1], q[0])
qc.cx(q[3], q[2])
qc.cx(q[5], q[4])
qc.cx(q[7], q[6])
qc.rx(np.pi * -0.5, q[1])
qc.rx(np.pi * -0.5, q[3])
qc.rx(np.pi * -0.5, q[5])
qc.rx(np.pi * -0.5, q[7])
qc.rz(np.pi * 0.5, q[1])
qc.rz(np.pi * 0.5, q[3])
qc.rz(np.pi * 0.5, q[5])
qc.rz(np.pi * 0.5, q[7])
qc.cx(q[0], q[1])
qc.cx(q[2], q[3])
qc.cx(q[4], q[5])
qc.cx(q[6], q[7])
qc.u3(np.pi * 1, 0, np.pi * 0.5, q[0])
qc.u3(np.pi * 1, 0, np.pi * 1.5, q[1])
qc.u3(np.pi * 1, 0, np.pi * 0.5, q[2])
qc.u3(np.pi * 1, 0, np.pi * 1.5, q[3])
qc.u3(np.pi * 1, 0, np.pi * 0.5, q[4])
qc.u3(np.pi * 1, 0, np.pi * 1.5, q[5])
qc.u3(np.pi * 1, 0, np.pi * 0.5, q[6])
qc.u3(np.pi * 1, 0, np.pi * 1.5, q[7])
qc.u3(np.pi * 0.5, np.pi * 1.5, np.pi * 1.5, q[0])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[1])
qc.u3(np.pi * 0.5, np.pi * 1.5, np.pi * 1.5, q[2])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[3])
qc.u3(np.pi * 0.5, np.pi * 1.5, np.pi * 1.5, q[4])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[5])
qc.u3(np.pi * 0.5, np.pi * 1.5, np.pi * 1.5, q[6])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[7])
qc.rx(np.pi * 0.5, q[0])
qc.rx(np.pi * 0.5, q[2])
qc.rx(np.pi * 0.5, q[4])
qc.rx(np.pi * 0.5, q[6])
qc.cx(q[0], q[1])
qc.cx(q[2], q[3])
qc.cx(q[4], q[5])
qc.cx(q[6], q[7])
qc.rx(np.pi * 0.4, q[0])
qc.ry(np.pi * 0.5, q[1])
qc.rx(np.pi * 0.4, q[2])
qc.ry(np.pi * 0.5, q[3])
qc.rx(np.pi * 0.4, q[4])
qc.ry(np.pi * 0.5, q[5])
qc.rx(np.pi * 0.4, q[6])
qc.ry(np.pi * 0.5, q[7])
qc.cx(q[1], q[0])
qc.cx(q[3], q[2])
qc.cx(q[5], q[4])
qc.cx(q[7], q[6])
qc.rx(np.pi * -0.5, q[1])
qc.rx(np.pi * -0.5, q[3])
qc.rx(np.pi * -0.5, q[5])
qc.rx(np.pi * -0.5, q[7])
qc.rz(np.pi * 0.5, q[1])
qc.rz(np.pi * 0.5, q[3])
qc.rz(np.pi * 0.5, q[5])
qc.rz(np.pi * 0.5, q[7])
qc.cx(q[0], q[1])
qc.cx(q[2], q[3])
qc.cx(q[4], q[5])
qc.cx(q[6], q[7])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 0.5, q[0])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[1])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 0.5, q[2])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[3])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 0.5, q[4])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[5])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 0.5, q[6])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[7])
qc.rx(np.pi * 0.3501408748, q[0])
qc.rx(np.pi * 0.3501408748, q[1])
qc.rx(np.pi * 0.3501408748, q[2])
qc.rx(np.pi * 0.3501408748, q[3])
qc.rx(np.pi * 0.3501408748, q[4])
qc.rx(np.pi * 0.3501408748, q[5])
qc.rx(np.pi * 0.3501408748, q[6])
qc.rx(np.pi * 0.3501408748, q[7])
qc.ry(np.pi * 0.3501408748, q[0])
qc.ry(np.pi * 0.3501408748, q[1])
qc.ry(np.pi * 0.3501408748, q[2])
qc.ry(np.pi * 0.3501408748, q[3])
qc.ry(np.pi * 0.3501408748, q[4])
qc.ry(np.pi * 0.3501408748, q[5])
qc.ry(np.pi * 0.3501408748, q[6])
qc.ry(np.pi * 0.3501408748, q[7])
qc.rz(np.pi * 0.3501408748, q[0])
qc.rz(np.pi * 0.3501408748, q[1])
qc.rz(np.pi * 0.3501408748, q[2])
qc.rz(np.pi * 0.3501408748, q[3])
qc.rz(np.pi * 0.3501408748, q[4])
qc.rz(np.pi * 0.3501408748, q[5])
qc.rz(np.pi * 0.3501408748, q[6])
qc.rz(np.pi * 0.3501408748, q[7])
qc.rx(np.pi * 0.3501408748, q[0])
qc.rx(np.pi * 0.3501408748, q[1])
qc.rx(np.pi * 0.3501408748, q[2])
qc.rx(np.pi * 0.3501408748, q[3])
qc.rx(np.pi * 0.3501408748, q[4])
qc.rx(np.pi * 0.3501408748, q[5])
qc.rx(np.pi * 0.3501408748, q[6])
qc.rx(np.pi * 0.3501408748, q[7])
qc.ry(np.pi * 0.3501408748, q[0])
qc.ry(np.pi * 0.3501408748, q[1])
qc.ry(np.pi * 0.3501408748, q[2])
qc.ry(np.pi * 0.3501408748, q[3])
qc.ry(np.pi * 0.3501408748, q[4])
qc.ry(np.pi * 0.3501408748, q[5])
qc.ry(np.pi * 0.3501408748, q[6])
qc.ry(np.pi * 0.3501408748, q[7])
qc.rz(np.pi * 0.3501408748, q[0])
qc.rz(np.pi * 0.3501408748, q[1])
qc.rz(np.pi * 0.3501408748, q[2])
qc.rz(np.pi * 0.3501408748, q[3])
qc.rz(np.pi * 0.3501408748, q[4])
qc.rz(np.pi * 0.3501408748, q[5])
qc.rz(np.pi * 0.3501408748, q[6])
qc.rz(np.pi * 0.3501408748, q[7])
qc.rz(np.pi * 1.1, q[0])
qc.rz(np.pi * 1.1, q[1])
qc.rz(np.pi * 1.1, q[2])
qc.rz(np.pi * 1.1, q[3])
qc.rz(np.pi * 1.1, q[4])
qc.rz(np.pi * 1.1, q[5])
qc.rz(np.pi * 1.1, q[6])
qc.rz(np.pi * 1.1, q[7])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[0])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[1])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[2])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[3])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[4])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[5])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[6])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[7])
qc.rx(np.pi * 0.5, q[1])
qc.rx(np.pi * 0.5, q[3])
qc.rx(np.pi * 0.5, q[5])
qc.rx(np.pi * 0.5, q[7])
qc.cx(q[1], q[2])
qc.cx(q[3], q[4])
qc.cx(q[5], q[6])
qc.rx(np.pi * 0.4, q[1])
qc.ry(np.pi * 0.5, q[2])
qc.rx(np.pi * 0.4, q[3])
qc.ry(np.pi * 0.5, q[4])
qc.rx(np.pi * 0.4, q[5])
qc.ry(np.pi * 0.5, q[6])
qc.cx(q[2], q[1])
qc.cx(q[4], q[3])
qc.cx(q[6], q[5])
qc.rx(np.pi * -0.5, q[2])
qc.rx(np.pi * -0.5, q[4])
qc.rx(np.pi * -0.5, q[6])
qc.rz(np.pi * 0.5, q[2])
qc.rz(np.pi * 0.5, q[4])
qc.rz(np.pi * 0.5, q[6])
qc.cx(q[1], q[2])
qc.cx(q[3], q[4])
qc.cx(q[5], q[6])
qc.u3(np.pi * 0.5, np.pi * 0.65, np.pi * 1, q[1])
qc.u3(np.pi * 0.5, np.pi * 0.15, 0, q[2])
qc.u3(np.pi * 0.5, np.pi * 0.65, np.pi * 1, q[3])
qc.u3(np.pi * 0.5, np.pi * 0.15, 0, q[4])
qc.u3(np.pi * 0.5, np.pi * 0.65, np.pi * 1, q[5])
qc.u3(np.pi * 0.5, np.pi * 0.15, 0, q[6])
qc.u3(0, np.pi * 1, np.pi * 0.5, q[1])
qc.u3(0, 0, np.pi * 0.5, q[2])
qc.u3(0, np.pi * 1, np.pi * 0.5, q[3])
qc.u3(0, 0, np.pi * 0.5, q[4])
qc.u3(0, np.pi * 1, np.pi * 0.5, q[5])
qc.u3(0, 0, np.pi * 0.5, q[6])
qc.rx(np.pi * 0.5, q[1])
qc.rx(np.pi * 0.5, q[3])
qc.rx(np.pi * 0.5, q[5])
qc.cx(q[1], q[2])
qc.cx(q[3], q[4])
qc.cx(q[5], q[6])
qc.rx(np.pi * 0.4, q[1])
qc.ry(np.pi * 0.5, q[2])
qc.rx(np.pi * 0.4, q[3])
qc.ry(np.pi * 0.5, q[4])
qc.rx(np.pi * 0.4, q[5])
qc.ry(np.pi * 0.5, q[6])
qc.cx(q[2], q[1])
qc.cx(q[4], q[3])
qc.cx(q[6], q[5])
qc.rx(np.pi * -0.5, q[2])
qc.rx(np.pi * -0.5, q[4])
qc.rx(np.pi * -0.5, q[6])
qc.rz(np.pi * 0.5, q[2])
qc.rz(np.pi * 0.5, q[4])
qc.rz(np.pi * 0.5, q[6])
qc.cx(q[1], q[2])
qc.cx(q[3], q[4])
qc.cx(q[5], q[6])
qc.u3(np.pi * 1, 0, np.pi * 0.5, q[1])
qc.u3(np.pi * 1, 0, np.pi * 1.5, q[2])
qc.u3(np.pi * 1, 0, np.pi * 0.5, q[3])
qc.u3(np.pi * 1, 0, np.pi * 1.5, q[4])
qc.u3(np.pi * 1, 0, np.pi * 0.5, q[5])
qc.u3(np.pi * 1, 0, np.pi * 1.5, q[6])
qc.u3(np.pi * 0.5, np.pi * 1.5, np.pi * 1.5, q[1])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[2])
qc.u3(np.pi * 0.5, np.pi * 1.5, np.pi * 1.5, q[3])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[4])
qc.u3(np.pi * 0.5, np.pi * 1.5, np.pi * 1.5, q[5])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[6])
qc.rx(np.pi * 0.5, q[1])
qc.rx(np.pi * 0.5, q[3])
qc.rx(np.pi * 0.5, q[5])
qc.cx(q[1], q[2])
qc.cx(q[3], q[4])
qc.cx(q[5], q[6])
qc.rx(np.pi * 0.4, q[1])
qc.ry(np.pi * 0.5, q[2])
qc.rx(np.pi * 0.4, q[3])
qc.ry(np.pi * 0.5, q[4])
qc.rx(np.pi * 0.4, q[5])
qc.ry(np.pi * 0.5, q[6])
qc.cx(q[2], q[1])
qc.cx(q[4], q[3])
qc.cx(q[6], q[5])
qc.rx(np.pi * -0.5, q[2])
qc.rx(np.pi * -0.5, q[4])
qc.rx(np.pi * -0.5, q[6])
qc.rz(np.pi * 0.5, q[2])
qc.rz(np.pi * 0.5, q[4])
qc.rz(np.pi * 0.5, q[6])
qc.cx(q[1], q[2])
qc.cx(q[3], q[4])
qc.cx(q[5], q[6])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 0.5, q[1])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[2])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 0.5, q[3])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[4])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 0.5, q[5])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[6])
qc.rx(np.pi * 0.3501408748, q[1])
qc.rx(np.pi * 0.3501408748, q[2])
qc.rx(np.pi * 0.3501408748, q[3])
qc.rx(np.pi * 0.3501408748, q[4])
qc.rx(np.pi * 0.3501408748, q[5])
qc.rx(np.pi * 0.3501408748, q[6])
qc.ry(np.pi * 0.3501408748, q[1])
qc.ry(np.pi * 0.3501408748, q[2])
qc.ry(np.pi * 0.3501408748, q[3])
qc.ry(np.pi * 0.3501408748, q[4])
qc.ry(np.pi * 0.3501408748, q[5])
qc.ry(np.pi * 0.3501408748, q[6])
qc.rz(np.pi * 0.3501408748, q[1])
qc.rz(np.pi * 0.3501408748, q[2])
qc.rz(np.pi * 0.3501408748, q[3])
qc.rz(np.pi * 0.3501408748, q[4])
qc.rz(np.pi * 0.3501408748, q[5])
qc.rz(np.pi * 0.3501408748, q[6])
qc.cx(q[7], q[0])
qc.ry(np.pi * 0.5, q[0])
qc.rx(np.pi * 0.4, q[7])
qc.cx(q[0], q[7])
qc.rx(np.pi * -0.5, q[0])
qc.rz(np.pi * 0.5, q[0])
qc.cx(q[7], q[0])
qc.u3(np.pi * 0.5, np.pi * 0.15, 0, q[0])
qc.u3(np.pi * 0.5, np.pi * 0.65, np.pi * 1, q[7])
qc.u3(0, 0, np.pi * 0.5, q[0])
qc.u3(0, np.pi * 1, np.pi * 0.5, q[7])
qc.rx(np.pi * 0.5, q[7])
qc.cx(q[7], q[0])
qc.ry(np.pi * 0.5, q[0])
qc.rx(np.pi * 0.4, q[7])
qc.cx(q[0], q[7])
qc.rx(np.pi * -0.5, q[0])
qc.rz(np.pi * 0.5, q[0])
qc.cx(q[7], q[0])
qc.u3(np.pi * 1, 0, np.pi * 1.5, q[0])
qc.u3(np.pi * 1, 0, np.pi * 0.5, q[7])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[0])
qc.u3(np.pi * 0.5, np.pi * 1.5, np.pi * 1.5, q[7])
qc.rx(np.pi * 0.5, q[7])
qc.cx(q[7], q[0])
qc.ry(np.pi * 0.5, q[0])
qc.rx(np.pi * 0.4, q[7])
qc.cx(q[0], q[7])
qc.rx(np.pi * -0.5, q[0])
qc.rz(np.pi * 0.5, q[0])
qc.cx(q[7], q[0])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[0])
qc.ry(np.pi * -0.5, q[1])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[2])
qc.ry(np.pi * -0.5, q[3])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[4])
qc.ry(np.pi * -0.5, q[5])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[6])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 0.5, q[7])
qc.rx(np.pi * 0.3501408748, q[0])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[1])
qc.rx(np.pi * 0.5, q[2])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[3])
qc.rx(np.pi * 0.5, q[4])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[5])
qc.rx(np.pi * 0.5, q[6])
qc.rx(np.pi * 0.3501408748, q[7])
qc.ry(np.pi * 0.3501408748, q[0])
qc.cx(q[2], q[3])
qc.cx(q[4], q[5])
qc.ry(np.pi * 0.3501408748, q[7])
qc.rz(np.pi * 0.3501408748, q[0])
qc.rx(np.pi * 0.05, q[2])
qc.ry(np.pi * 0.5, q[3])
qc.rx(np.pi * 0.05, q[4])
qc.ry(np.pi * 0.5, q[5])
qc.rz(np.pi * 0.3501408748, q[7])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[0])
qc.cx(q[3], q[2])
qc.cx(q[5], q[4])
qc.ry(np.pi * -0.5, q[7])
qc.rx(np.pi * 0.5, q[0])
qc.rx(np.pi * -0.5, q[3])
qc.rx(np.pi * -0.5, q[5])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[7])
qc.cx(q[0], q[1])
qc.rz(np.pi * 0.5, q[3])
qc.rz(np.pi * 0.5, q[5])
qc.cx(q[6], q[7])
qc.rx(np.pi * 0.05, q[0])
qc.ry(np.pi * 0.5, q[1])
qc.cx(q[2], q[3])
qc.cx(q[4], q[5])
qc.rx(np.pi * 0.05, q[6])
qc.ry(np.pi * 0.5, q[7])
qc.cx(q[1], q[0])
qc.u3(np.pi * 0.5, np.pi * 0.3, np.pi * 1, q[2])
qc.u3(np.pi * 0.5, np.pi * 1.8, 0, q[3])
qc.u3(np.pi * 0.5, np.pi * 0.3, np.pi * 1, q[4])
qc.u3(np.pi * 0.5, np.pi * 1.8, 0, q[5])
qc.cx(q[7], q[6])
qc.rx(np.pi * -0.5, q[1])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[2])
qc.ry(np.pi * 0.5, q[3])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[4])
qc.ry(np.pi * 0.5, q[5])
qc.rx(np.pi * -0.5, q[7])
qc.rz(np.pi * 0.5, q[1])
qc.rx(np.pi * 0.5, q[2])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[3])
qc.rx(np.pi * 0.5, q[4])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[5])
qc.rz(np.pi * 0.5, q[7])
qc.cx(q[0], q[1])
qc.cx(q[2], q[3])
qc.cx(q[4], q[5])
qc.cx(q[6], q[7])
qc.u3(np.pi * 0.5, np.pi * 0.3, np.pi * 1, q[0])
qc.u3(np.pi * 0.5, np.pi * 1.8, 0, q[1])
qc.rx(np.pi * 0.05, q[2])
qc.ry(np.pi * 0.5, q[3])
qc.rx(np.pi * 0.05, q[4])
qc.ry(np.pi * 0.5, q[5])
qc.u3(np.pi * 0.5, np.pi * 0.3, np.pi * 1, q[6])
qc.u3(np.pi * 0.5, np.pi * 1.8, 0, q[7])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[0])
qc.ry(np.pi * 0.5, q[1])
qc.cx(q[3], q[2])
qc.cx(q[5], q[4])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[6])
qc.ry(np.pi * 0.5, q[7])
qc.rx(np.pi * 0.5, q[0])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[1])
qc.rx(np.pi * -0.5, q[3])
qc.rx(np.pi * -0.5, q[5])
qc.rx(np.pi * 0.5, q[6])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[7])
qc.cx(q[0], q[1])
qc.rz(np.pi * 0.5, q[3])
qc.rz(np.pi * 0.5, q[5])
qc.cx(q[6], q[7])
qc.rx(np.pi * 0.05, q[0])
qc.ry(np.pi * 0.5, q[1])
qc.cx(q[2], q[3])
qc.cx(q[4], q[5])
qc.rx(np.pi * 0.05, q[6])
qc.ry(np.pi * 0.5, q[7])
qc.cx(q[1], q[0])
qc.u3(np.pi * 0.5, np.pi * 0.3, np.pi * 1, q[2])
qc.u3(np.pi * 0.5, np.pi * 1.8, 0, q[3])
qc.u3(np.pi * 0.5, np.pi * 0.3, np.pi * 1, q[4])
qc.u3(np.pi * 0.5, np.pi * 1.8, 0, q[5])
qc.cx(q[7], q[6])
qc.rx(np.pi * -0.5, q[1])
qc.ry(np.pi * -0.5, q[2])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[3])
qc.ry(np.pi * -0.5, q[4])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[5])
qc.rx(np.pi * -0.5, q[7])
qc.rz(np.pi * 0.5, q[1])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[2])
qc.rx(np.pi * 0.5, q[3])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[4])
qc.rx(np.pi * 0.5, q[5])
qc.rz(np.pi * 0.5, q[7])
qc.cx(q[0], q[1])
qc.cx(q[3], q[4])
qc.cx(q[6], q[7])
qc.u3(np.pi * 0.5, np.pi * 0.3, np.pi * 1, q[0])
qc.u3(np.pi * 0.5, np.pi * 1.8, 0, q[1])
qc.rx(np.pi * 0.05, q[3])
qc.ry(np.pi * 0.5, q[4])
qc.u3(np.pi * 0.5, np.pi * 0.3, np.pi * 1, q[6])
qc.u3(np.pi * 0.5, np.pi * 1.8, 0, q[7])
qc.ry(np.pi * -0.5, q[0])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[1])
qc.cx(q[4], q[3])
qc.ry(np.pi * -0.5, q[6])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[7])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[0])
qc.rx(np.pi * 0.5, q[1])
qc.rx(np.pi * -0.5, q[4])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[6])
qc.rx(np.pi * 0.5, q[7])
qc.cx(q[1], q[2])
qc.rz(np.pi * 0.5, q[4])
qc.cx(q[5], q[6])
qc.rx(np.pi * 0.05, q[1])
qc.ry(np.pi * 0.5, q[2])
qc.cx(q[3], q[4])
qc.rx(np.pi * 0.05, q[5])
qc.ry(np.pi * 0.5, q[6])
qc.cx(q[2], q[1])
qc.u3(np.pi * 0.5, np.pi * 0.3, np.pi * 1, q[3])
qc.u3(np.pi * 0.5, np.pi * 1.8, 0, q[4])
qc.cx(q[6], q[5])
qc.rx(np.pi * -0.5, q[2])
qc.ry(np.pi * 0.5, q[4])
qc.rx(np.pi * -0.5, q[6])
qc.rz(np.pi * 0.5, q[2])
qc.rz(np.pi * 0.5, q[6])
qc.cx(q[1], q[2])
qc.cx(q[5], q[6])
qc.u3(np.pi * 0.5, np.pi * 0.3, np.pi * 1, q[1])
qc.u3(np.pi * 0.5, np.pi * 1.8, 0, q[2])
qc.u3(np.pi * 0.5, np.pi * 0.3, np.pi * 1, q[5])
qc.u3(np.pi * 0.5, np.pi * 1.8, 0, q[6])
qc.ry(np.pi * 0.5, q[2])
qc.ry(np.pi * 0.5, q[6])
qc.cx(q[7], q[0])
qc.ry(np.pi * 0.5, q[0])
qc.rx(np.pi * 0.05, q[7])
qc.cx(q[0], q[7])
qc.rx(np.pi * -0.5, q[0])
qc.rz(np.pi * 0.5, q[0])
qc.cx(q[7], q[0])
qc.u3(np.pi * 0.5, np.pi * 1.8, 0, q[0])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[1])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[2])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[3])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[4])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[5])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[6])
qc.u3(np.pi * 0.5, np.pi * 0.3, np.pi * 1, q[7])
qc.ry(np.pi * 0.5, q[0])
qc.rx(np.pi * 0.5, q[1])
qc.rx(np.pi * 0.5, q[3])
qc.rx(np.pi * 0.5, q[5])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[7])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[0])
qc.cx(q[1], q[2])
qc.cx(q[3], q[4])
qc.cx(q[5], q[6])
qc.rx(np.pi * 0.5, q[7])
qc.rx(np.pi * 0.05, q[1])
qc.ry(np.pi * 0.5, q[2])
qc.rx(np.pi * 0.05, q[3])
qc.ry(np.pi * 0.5, q[4])
qc.rx(np.pi * 0.05, q[5])
qc.ry(np.pi * 0.5, q[6])
qc.cx(q[2], q[1])
qc.cx(q[4], q[3])
qc.cx(q[6], q[5])
qc.rx(np.pi * -0.5, q[2])
qc.rx(np.pi * -0.5, q[4])
qc.rx(np.pi * -0.5, q[6])
qc.rz(np.pi * 0.5, q[2])
qc.rz(np.pi * 0.5, q[4])
qc.rz(np.pi * 0.5, q[6])
qc.cx(q[1], q[2])
qc.cx(q[3], q[4])
qc.cx(q[5], q[6])
qc.u3(np.pi * 0.5, np.pi * 0.3, np.pi * 1, q[1])
qc.u3(np.pi * 0.5, np.pi * 1.8, 0, q[2])
qc.u3(np.pi * 0.5, np.pi * 0.3, np.pi * 1, q[3])
qc.u3(np.pi * 0.5, np.pi * 1.8, 0, q[4])
qc.u3(np.pi * 0.5, np.pi * 0.3, np.pi * 1, q[5])
qc.u3(np.pi * 0.5, np.pi * 1.8, 0, q[6])
qc.cx(q[7], q[0])
qc.ry(np.pi * 0.5, q[0])
qc.rx(np.pi * 0.05, q[7])
qc.cx(q[0], q[7])
qc.rx(np.pi * -0.5, q[0])
qc.rz(np.pi * 0.5, q[0])
qc.cx(q[7], q[0])
qc.u3(np.pi * 0.5, np.pi * 1.8, 0, q[0])
qc.rx(np.pi * 0.3501408748, q[1])
qc.rx(np.pi * 0.3501408748, q[2])
qc.rx(np.pi * 0.3501408748, q[3])
qc.rx(np.pi * 0.3501408748, q[4])
qc.rx(np.pi * 0.3501408748, q[5])
qc.rx(np.pi * 0.3501408748, q[6])
qc.u3(np.pi * 0.5, np.pi * 0.3, np.pi * 1, q[7])
qc.rx(np.pi * 0.3501408748, q[0])
qc.ry(np.pi * 0.3501408748, q[1])
qc.ry(np.pi * 0.3501408748, q[2])
qc.ry(np.pi * 0.3501408748, q[3])
qc.ry(np.pi * 0.3501408748, q[4])
qc.ry(np.pi * 0.3501408748, q[5])
qc.ry(np.pi * 0.3501408748, q[6])
qc.rx(np.pi * 0.3501408748, q[7])
qc.ry(np.pi * 0.3501408748, q[0])
qc.rz(np.pi * 0.3501408748, q[1])
qc.rz(np.pi * 0.3501408748, q[2])
qc.rz(np.pi * 0.3501408748, q[3])
qc.rz(np.pi * 0.3501408748, q[4])
qc.rz(np.pi * 0.3501408748, q[5])
qc.rz(np.pi * 0.3501408748, q[6])
qc.ry(np.pi * 0.3501408748, q[7])
qc.rz(np.pi * 0.3501408748, q[0])
qc.rz(np.pi * 1.1, q[1])
qc.rz(np.pi * 1.1, q[2])
qc.rz(np.pi * 1.1, q[3])
qc.rz(np.pi * 1.1, q[4])
qc.rz(np.pi * 1.1, q[5])
qc.rz(np.pi * 1.1, q[6])
qc.rz(np.pi * 0.3501408748, q[7])
qc.rz(np.pi * 1.1, q[0])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[1])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[2])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[3])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[4])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[5])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[6])
qc.rz(np.pi * 1.1, q[7])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[0])
qc.rx(np.pi * 0.5, q[2])
qc.rx(np.pi * 0.5, q[4])
qc.rx(np.pi * 0.5, q[6])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[7])
qc.rx(np.pi * 0.5, q[0])
qc.cx(q[2], q[3])
qc.cx(q[4], q[5])
qc.cx(q[6], q[7])
qc.cx(q[0], q[1])
qc.rx(np.pi * 0.4, q[2])
qc.ry(np.pi * 0.5, q[3])
qc.rx(np.pi * 0.4, q[4])
qc.ry(np.pi * 0.5, q[5])
qc.rx(np.pi * 0.4, q[6])
qc.ry(np.pi * 0.5, q[7])
qc.rx(np.pi * 0.4, q[0])
qc.ry(np.pi * 0.5, q[1])
qc.cx(q[3], q[2])
qc.cx(q[5], q[4])
qc.cx(q[7], q[6])
qc.cx(q[1], q[0])
qc.rx(np.pi * -0.5, q[3])
qc.rx(np.pi * -0.5, q[5])
qc.rx(np.pi * -0.5, q[7])
qc.rx(np.pi * -0.5, q[1])
qc.rz(np.pi * 0.5, q[3])
qc.rz(np.pi * 0.5, q[5])
qc.rz(np.pi * 0.5, q[7])
qc.rz(np.pi * 0.5, q[1])
qc.cx(q[2], q[3])
qc.cx(q[4], q[5])
qc.cx(q[6], q[7])
qc.cx(q[0], q[1])
qc.u3(np.pi * 0.5, np.pi * 0.65, np.pi * 1, q[2])
qc.u3(np.pi * 0.5, np.pi * 0.15, 0, q[3])
qc.u3(np.pi * 0.5, np.pi * 0.65, np.pi * 1, q[4])
qc.u3(np.pi * 0.5, np.pi * 0.15, 0, q[5])
qc.u3(np.pi * 0.5, np.pi * 0.65, np.pi * 1, q[6])
qc.u3(np.pi * 0.5, np.pi * 0.15, 0, q[7])
qc.u3(np.pi * 0.5, np.pi * 0.65, np.pi * 1, q[0])
qc.u3(np.pi * 0.5, np.pi * 0.15, 0, q[1])
qc.u3(0, np.pi * 1, np.pi * 0.5, q[2])
qc.u3(0, 0, np.pi * 0.5, q[3])
qc.u3(0, np.pi * 1, np.pi * 0.5, q[4])
qc.u3(0, 0, np.pi * 0.5, q[5])
qc.u3(0, np.pi * 1, np.pi * 0.5, q[6])
qc.u3(0, 0, np.pi * 0.5, q[7])
qc.u3(0, np.pi * 1, np.pi * 0.5, q[0])
qc.u3(0, 0, np.pi * 0.5, q[1])
qc.rx(np.pi * 0.5, q[2])
qc.rx(np.pi * 0.5, q[4])
qc.rx(np.pi * 0.5, q[6])
qc.rx(np.pi * 0.5, q[0])
qc.cx(q[2], q[3])
qc.cx(q[4], q[5])
qc.cx(q[6], q[7])
qc.cx(q[0], q[1])
qc.rx(np.pi * 0.4, q[2])
qc.ry(np.pi * 0.5, q[3])
qc.rx(np.pi * 0.4, q[4])
qc.ry(np.pi * 0.5, q[5])
qc.rx(np.pi * 0.4, q[6])
qc.ry(np.pi * 0.5, q[7])
qc.rx(np.pi * 0.4, q[0])
qc.ry(np.pi * 0.5, q[1])
qc.cx(q[3], q[2])
qc.cx(q[5], q[4])
qc.cx(q[7], q[6])
qc.cx(q[1], q[0])
qc.rx(np.pi * -0.5, q[3])
qc.rx(np.pi * -0.5, q[5])
qc.rx(np.pi * -0.5, q[7])
qc.rx(np.pi * -0.5, q[1])
qc.rz(np.pi * 0.5, q[3])
qc.rz(np.pi * 0.5, q[5])
qc.rz(np.pi * 0.5, q[7])
qc.rz(np.pi * 0.5, q[1])
qc.cx(q[2], q[3])
qc.cx(q[4], q[5])
qc.cx(q[6], q[7])
qc.cx(q[0], q[1])
qc.u3(np.pi * 1, 0, np.pi * 0.5, q[2])
qc.u3(np.pi * 1, 0, np.pi * 1.5, q[3])
qc.u3(np.pi * 1, 0, np.pi * 0.5, q[4])
qc.u3(np.pi * 1, 0, np.pi * 1.5, q[5])
qc.u3(np.pi * 1, 0, np.pi * 0.5, q[6])
qc.u3(np.pi * 1, 0, np.pi * 1.5, q[7])
qc.u3(np.pi * 1, 0, np.pi * 0.5, q[0])
qc.u3(np.pi * 1, 0, np.pi * 1.5, q[1])
qc.u3(np.pi * 0.5, np.pi * 1.5, np.pi * 1.5, q[2])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[3])
qc.u3(np.pi * 0.5, np.pi * 1.5, np.pi * 1.5, q[4])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[5])
qc.u3(np.pi * 0.5, np.pi * 1.5, np.pi * 1.5, q[6])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[7])
qc.u3(np.pi * 0.5, np.pi * 1.5, np.pi * 1.5, q[0])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[1])
qc.rx(np.pi * 0.5, q[2])
qc.rx(np.pi * 0.5, q[4])
qc.rx(np.pi * 0.5, q[6])
qc.rx(np.pi * 0.5, q[0])
qc.cx(q[2], q[3])
qc.cx(q[4], q[5])
qc.cx(q[6], q[7])
qc.cx(q[0], q[1])
qc.rx(np.pi * 0.4, q[2])
qc.ry(np.pi * 0.5, q[3])
qc.rx(np.pi * 0.4, q[4])
qc.ry(np.pi * 0.5, q[5])
qc.rx(np.pi * 0.4, q[6])
qc.ry(np.pi * 0.5, q[7])
qc.rx(np.pi * 0.4, q[0])
qc.ry(np.pi * 0.5, q[1])
qc.cx(q[3], q[2])
qc.cx(q[5], q[4])
qc.cx(q[7], q[6])
qc.cx(q[1], q[0])
qc.rx(np.pi * -0.5, q[3])
qc.rx(np.pi * -0.5, q[5])
qc.rx(np.pi * -0.5, q[7])
qc.rx(np.pi * -0.5, q[1])
qc.rz(np.pi * 0.5, q[3])
qc.rz(np.pi * 0.5, q[5])
qc.rz(np.pi * 0.5, q[7])
qc.rz(np.pi * 0.5, q[1])
qc.cx(q[2], q[3])
qc.cx(q[4], q[5])
qc.cx(q[6], q[7])
qc.cx(q[0], q[1])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 0.5, q[2])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[3])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 0.5, q[4])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[5])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 0.5, q[6])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[7])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 0.5, q[0])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[1])
qc.rx(np.pi * 0.3501408748, q[2])
qc.rx(np.pi * 0.3501408748, q[3])
qc.rx(np.pi * 0.3501408748, q[4])
qc.rx(np.pi * 0.3501408748, q[5])
qc.rx(np.pi * 0.3501408748, q[6])
qc.rx(np.pi * 0.3501408748, q[7])
qc.rx(np.pi * 0.3501408748, q[0])
qc.rx(np.pi * 0.3501408748, q[1])
qc.ry(np.pi * 0.3501408748, q[2])
qc.ry(np.pi * 0.3501408748, q[3])
qc.ry(np.pi * 0.3501408748, q[4])
qc.ry(np.pi * 0.3501408748, q[5])
qc.ry(np.pi * 0.3501408748, q[6])
qc.ry(np.pi * 0.3501408748, q[7])
qc.ry(np.pi * 0.3501408748, q[0])
qc.ry(np.pi * 0.3501408748, q[1])
qc.rz(np.pi * 0.3501408748, q[2])
qc.rz(np.pi * 0.3501408748, q[3])
qc.rz(np.pi * 0.3501408748, q[4])
qc.rz(np.pi * 0.3501408748, q[5])
qc.rz(np.pi * 0.3501408748, q[6])
qc.rz(np.pi * 0.3501408748, q[7])
qc.rz(np.pi * 0.3501408748, q[0])
qc.rz(np.pi * 0.3501408748, q[1])
qc.rx(np.pi * 0.3501408748, q[2])
qc.rx(np.pi * 0.3501408748, q[3])
qc.rx(np.pi * 0.3501408748, q[4])
qc.rx(np.pi * 0.3501408748, q[5])
qc.rx(np.pi * 0.3501408748, q[6])
qc.rx(np.pi * 0.3501408748, q[7])
qc.rx(np.pi * 0.3501408748, q[0])
qc.rx(np.pi * 0.3501408748, q[1])
qc.ry(np.pi * 0.3501408748, q[2])
qc.ry(np.pi * 0.3501408748, q[3])
qc.ry(np.pi * 0.3501408748, q[4])
qc.ry(np.pi * 0.3501408748, q[5])
qc.ry(np.pi * 0.3501408748, q[6])
qc.ry(np.pi * 0.3501408748, q[7])
qc.ry(np.pi * 0.3501408748, q[0])
qc.ry(np.pi * 0.3501408748, q[1])
qc.rz(np.pi * 0.3501408748, q[2])
qc.rz(np.pi * 0.3501408748, q[3])
qc.rz(np.pi * 0.3501408748, q[4])
qc.rz(np.pi * 0.3501408748, q[5])
qc.rz(np.pi * 0.3501408748, q[6])
qc.rz(np.pi * 0.3501408748, q[7])
qc.rz(np.pi * 0.3501408748, q[0])
qc.rz(np.pi * 0.3501408748, q[1])
qc.rz(np.pi * 1.1, q[2])
qc.rz(np.pi * 1.1, q[3])
qc.rz(np.pi * 1.1, q[4])
qc.rz(np.pi * 1.1, q[5])
qc.rz(np.pi * 1.1, q[6])
qc.rz(np.pi * 1.1, q[7])
qc.rz(np.pi * 1.1, q[0])
qc.rz(np.pi * 1.1, q[1])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[2])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[3])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[4])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[5])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[6])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[7])
qc.u3(np.pi * 0.5, np.pi * 1, np.pi * 0.75, q[0])
qc.u3(np.pi * 0.5, 0, np.pi * 0.25, q[1])
qc.rx(np.pi * 0.5, q[3])
qc.rx(np.pi * 0.5, q[5])
qc.rx(np.pi * 0.5, q[7])
qc.rx(np.pi * 0.5, q[1])
qc.cx(q[3], q[4])
qc.cx(q[5], q[6])
qc.cx(q[1], q[2])
qc.rx(np.pi * 0.4, q[3])
qc.ry(np.pi * 0.5, q[4])
qc.rx(np.pi * 0.4, q[5])
qc.ry(np.pi * 0.5, q[6])
qc.rx(np.pi * 0.4, q[1])
qc.ry(np.pi * 0.5, q[2])
qc.cx(q[4], q[3])
qc.cx(q[6], q[5])
qc.cx(q[2], q[1])
qc.rx(np.pi * -0.5, q[4])
qc.rx(np.pi * -0.5, q[6])
qc.rx(np.pi * -0.5, q[2])
qc.rz(np.pi * 0.5, q[4])
qc.rz(np.pi * 0.5, q[6])
qc.rz(np.pi * 0.5, q[2])
qc.cx(q[3], q[4])
qc.cx(q[5], q[6])
qc.cx(q[1], q[2])
qc.u3(np.pi * 0.5, np.pi * 0.65, np.pi * 1, q[3])
qc.u3(np.pi * 0.5, np.pi * 0.15, 0, q[4])
qc.u3(np.pi * 0.5, np.pi * 0.65, np.pi * 1, q[5])
qc.u3(np.pi * 0.5, np.pi * 0.15, 0, q[6])
qc.u3(np.pi * 0.5, np.pi * 0.65, np.pi * 1, q[1])
qc.u3(np.pi * 0.5, np.pi * 0.15, 0, q[2])
qc.u3(0, np.pi * 1, np.pi * 0.5, q[3])
qc.u3(0, 0, np.pi * 0.5, q[4])
qc.u3(0, np.pi * 1, np.pi * 0.5, q[5])
qc.u3(0, 0, np.pi * 0.5, q[6])
qc.u3(0, np.pi * 1, np.pi * 0.5, q[1])
qc.u3(0, 0, np.pi * 0.5, q[2])
qc.rx(np.pi * 0.5, q[3])
qc.rx(np.pi * 0.5, q[5])
qc.rx(np.pi * 0.5, q[1])
qc.cx(q[3], q[4])
qc.cx(q[5], q[6])
qc.cx(q[1], q[2])
qc.rx(np.pi * 0.4, q[3])
qc.ry(np.pi * 0.5, q[4])
qc.rx(np.pi * 0.4, q[5])
qc.ry(np.pi * 0.5, q[6])
qc.rx(np.pi * 0.4, q[1])
qc.ry(np.pi * 0.5, q[2])
qc.cx(q[4], q[3])
qc.cx(q[6], q[5])
qc.cx(q[2], q[1])
qc.rx(np.pi * -0.5, q[4])
qc.rx(np.pi * -0.5, q[6])
qc.rx(np.pi * -0.5, q[2])
qc.rz(np.pi * 0.5, q[4])
qc.rz(np.pi * 0.5, q[6])
qc.rz(np.pi * 0.5, q[2])
qc.cx(q[3], q[4])
qc.cx(q[5], q[6])
qc.cx(q[1], q[2])
qc.u3(np.pi * 1, 0, np.pi * 0.5, q[3])
qc.u3(np.pi * 1, 0, np.pi * 1.5, q[4])
qc.u3(np.pi * 1, 0, np.pi * 0.5, q[5])
qc.u3(np.pi * 1, 0, np.pi * 1.5, q[6])
qc.u3(np.pi * 1, 0, np.pi * 0.5, q[1])
qc.u3(np.pi * 1, 0, np.pi * 1.5, q[2])
qc.u3(np.pi * 0.5, np.pi * 1.5, np.pi * 1.5, q[3])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[4])
qc.u3(np.pi * 0.5, np.pi * 1.5, np.pi * 1.5, q[5])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[6])
qc.u3(np.pi * 0.5, np.pi * 1.5, np.pi * 1.5, q[1])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[2])
qc.rx(np.pi * 0.5, q[3])
qc.rx(np.pi * 0.5, q[5])
qc.rx(np.pi * 0.5, q[1])
qc.cx(q[3], q[4])
qc.cx(q[5], q[6])
qc.cx(q[1], q[2])
qc.rx(np.pi * 0.4, q[3])
qc.ry(np.pi * 0.5, q[4])
qc.rx(np.pi * 0.4, q[5])
qc.ry(np.pi * 0.5, q[6])
qc.rx(np.pi * 0.4, q[1])
qc.ry(np.pi * 0.5, q[2])
qc.cx(q[4], q[3])
qc.cx(q[6], q[5])
qc.cx(q[2], q[1])
qc.rx(np.pi * -0.5, q[4])
qc.rx(np.pi * -0.5, q[6])
qc.rx(np.pi * -0.5, q[2])
qc.rz(np.pi * 0.5, q[4])
qc.rz(np.pi * 0.5, q[6])
qc.rz(np.pi * 0.5, q[2])
qc.cx(q[3], q[4])
qc.cx(q[5], q[6])
qc.cx(q[1], q[2])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 0.5, q[3])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[4])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 0.5, q[5])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[6])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 0.5, q[1])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[2])
qc.rx(np.pi * 0.3501408748, q[3])
qc.rx(np.pi * 0.3501408748, q[4])
qc.rx(np.pi * 0.3501408748, q[5])
qc.rx(np.pi * 0.3501408748, q[6])
qc.rx(np.pi * 0.3501408748, q[1])
qc.rx(np.pi * 0.3501408748, q[2])
qc.ry(np.pi * 0.3501408748, q[3])
qc.ry(np.pi * 0.3501408748, q[4])
qc.ry(np.pi * 0.3501408748, q[5])
qc.ry(np.pi * 0.3501408748, q[6])
qc.ry(np.pi * 0.3501408748, q[1])
qc.ry(np.pi * 0.3501408748, q[2])
qc.rz(np.pi * 0.3501408748, q[3])
qc.rz(np.pi * 0.3501408748, q[4])
qc.rz(np.pi * 0.3501408748, q[5])
qc.rz(np.pi * 0.3501408748, q[6])
qc.rz(np.pi * 0.3501408748, q[1])
qc.rz(np.pi * 0.3501408748, q[2])
qc.cx(q[7], q[0])
qc.ry(np.pi * 0.5, q[0])
qc.rx(np.pi * 0.4, q[7])
qc.cx(q[0], q[7])
qc.rx(np.pi * -0.5, q[0])
qc.rz(np.pi * 0.5, q[0])
qc.cx(q[7], q[0])
qc.u3(np.pi * 0.5, np.pi * 0.15, 0, q[0])
qc.u3(np.pi * 0.5, np.pi * 0.65, np.pi * 1, q[7])
qc.u3(0, 0, np.pi * 0.5, q[0])
qc.u3(0, np.pi * 1, np.pi * 0.5, q[7])
qc.rx(np.pi * 0.5, q[7])
qc.cx(q[7], q[0])
qc.ry(np.pi * 0.5, q[0])
qc.rx(np.pi * 0.4, q[7])
qc.cx(q[0], q[7])
qc.rx(np.pi * -0.5, q[0])
qc.rz(np.pi * 0.5, q[0])
qc.cx(q[7], q[0])
qc.u3(np.pi * 1, 0, np.pi * 1.5, q[0])
qc.u3(np.pi * 1, 0, np.pi * 0.5, q[7])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[0])
qc.u3(np.pi * 0.5, np.pi * 1.5, np.pi * 1.5, q[7])
qc.rx(np.pi * 0.5, q[7])
qc.cx(q[7], q[0])
qc.ry(np.pi * 0.5, q[0])
qc.rx(np.pi * 0.4, q[7])
qc.cx(q[0], q[7])
qc.rx(np.pi * -0.5, q[0])
qc.rz(np.pi * 0.5, q[0])
qc.cx(q[7], q[0])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 1.5, q[0])
qc.u3(np.pi * 0.5, np.pi * 0.5, np.pi * 0.5, q[7])
qc.rx(np.pi * 0.3501408748, q[0])
qc.rx(np.pi * 0.3501408748, q[7])
qc.ry(np.pi * 0.3501408748, q[0])
qc.ry(np.pi * 0.3501408748, q[7])
qc.rz(np.pi * 0.3501408748, q[0])
qc.rz(np.pi * 0.3501408748, q[7])
qc.measure(q[0], ans[0])
qc.measure(q[1], ans[1])
qc.measure(q[2], ans[2])
qc.measure(q[3], ans[3])
qc.measure(q[4], ans[4])
qc.measure(q[5], ans[5])
qc.measure(q[6], ans[6])
qc.measure(q[7], ans[7])

backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend=backend, shots=shots)
job_result = job.result()
print(job_result.get_counts(qc))
with open('qiskit.circuit', 'w') as f:
    print(qc.draw(), file=f)

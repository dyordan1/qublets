""" Entangled qubits (Bell pair) """

from qublets import QPU, QUInt

qpu = QPU(2)
a = QUInt.zeros(1, qpu=qpu).h()
b = QUInt.zeros(1, qpu=qpu).entangle(on=a[0])

print(qpu.states().debug_string())

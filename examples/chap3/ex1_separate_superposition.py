""" Separate qubits in superposition """

from qublets import QPU, QUInt

qpu = QPU(3)
q1 = QUInt.zeros(1, qpu=qpu)
q2 = QUInt.zeros(1, qpu=qpu).h()
q3 = QUInt.zeros(1, qpu=qpu).h()

print(qpu.states().debug_string())

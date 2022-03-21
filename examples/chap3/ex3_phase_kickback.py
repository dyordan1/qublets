""" Phase Kickback """

from math import pi
from qublets import QPU, QUInt

qpu = QPU(3)
r1 = QUInt.zeros(2, qpu=qpu).h()
r2 = QUInt.ones(1, qpu=qpu)
r2[0].c_phase(on=r1[0], angle=-pi / 4)
r2[0].c_phase(on=r1[1], angle=-pi / 2)

print(qpu.states().debug_string())

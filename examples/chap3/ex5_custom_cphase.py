""" Example of deconstructing c_phase """

from math import pi
from qublets import QPU, QUInt

qpu = QPU(2)
q1 = QUInt.pluses(1, qpu=qpu)
q2 = QUInt.pluses(1, qpu=qpu)

# Using two c_negate and three phase...
q2.phase(angle=pi / 4).c_negate(on=q1[0]).phase(angle=-pi /
                                                4).c_negate(on=q1[0])
q1.phase(angle=-pi / 4)

# Builds the same operation as a 2-qubit c_phase
q1.c_phase(on=q2[0], angle=pi / 2)

print(qpu.states().debug_string())

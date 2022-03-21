"""
This sample demonstrates construction of a ROOTNOT operation using HAD and PHASE
operations. It also demonstrates the built-in ROOTNOT operator to show that it
has the same effect. Note that applying ROOTNOT twice is the equivalent of a
single NOT operator.
"""

from qublets import QUInt

q1 = QUInt.zeros(1).h().phase().h()
print(q1.qpu.states().debug_string())

q1 = q1.h().phase().h()
print(q1.qpu.states().debug_string())

q1 = q1.sqrt_not()
print(q1.qpu.states().debug_string())

q1 = q1.sqrt_not()
print(q1.qpu.states().debug_string())

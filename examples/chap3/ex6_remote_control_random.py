""" remote-"Controlled" random number generator """

from math import pi
from qublets import QUInt, QPU

qpu = QPU(2)
a = QUInt.pluses(1, qpu=qpu)
b = QUInt.pluses(1, qpu=qpu).phase(angle=pi / 4).h()

# Entangle state
b.c_negate(on=a[0])
print(qpu.states().debug_string())

# Now, you can read *either* qubit and get 50% prob. If the result is 0, then
# the prob of the *remaining* qubit is 15%, else it's 85%
print(f"a: {a.measure()}")
print(f"b: {b.measure()}")

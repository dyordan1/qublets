""" This sample generates a single random bit. """

from qublets import QUInt

res = QUInt.zeros(1).h().measure()
print(res)

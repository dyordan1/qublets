"""
This sample generates a single random byte, using eight unentangled qubits.
"""

from qublets import QUInt

res = QUInt.zeros(8).h().measure()
print(res)

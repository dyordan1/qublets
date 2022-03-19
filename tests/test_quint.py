""" Tests for QUInt and QInt """

import unittest
from qublets import QPU, QUInt


class QUIntTest(unittest.TestCase):

  def test_num_qubits(self):
    q1 = QUInt.zeros(2)
    q2 = QUInt.zeros(10)

    self.assertEqual(q1.num_qubits, 2, "quint count mismatch")
    self.assertEqual(q2.num_qubits, 10, "quint count mismatch")

  def test_shared_qpu(self):
    qpu = QPU(4)
    q1 = QUInt.zeros(2, qpu)
    q2 = QUInt.zeros(2, qpu)

    self.assertEqual(q1.qpu, qpu, "quint qpu mismatch")
    self.assertEqual(q2.qpu, qpu, "quint qpu mismatch")

  def test_qubit_access(self):
    q1 = QUInt.zeros(2)
    qb1 = q1[0]
    qb2 = q1[1]

    self.assertEqual(qb1.quint, q1, "qubit access mismatch")
    self.assertEqual(qb1.qubit, 0, "qubit access mismatch")
    self.assertEqual(qb2.quint, q1, "qubit access mismatch")
    self.assertEqual(qb2.qubit, 1, "qubit access mismatch")

  def test_qubit_access_out_of_range(self):
    q1 = QUInt.zeros(2)

    def invalid_access():
      q1[2].measure()

    self.assertRaises(Exception, invalid_access)

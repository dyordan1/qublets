""" Tests for QPU-related functionality """

import math
import unittest
from qublets import QUInt


class QPUTest(unittest.TestCase):

  def test_zero_state(self):
    q1 = QUInt.zeros(4)
    states = q1.qpu.states()

    self.assertEqual(len(states),
                     1,
                     msg="Zero state should not contain other probabilities")
    self.assertEqual(states[0].value, 0, msg="Zero state value should be zero")
    self.assertAlmostEqual(states[0].probability,
                           1,
                           msg="Zero state probability should be 100%")
    self.assertAlmostEqual(states[0].phase,
                           0,
                           msg="Zero state phase should be zero")

  def test_one_state(self):
    q1 = QUInt.ones(4)
    states = q1.qpu.states()

    self.assertEqual(len(states),
                     1,
                     msg="One state should not contain other probabilities")
    self.assertEqual(states[0].value, 15, msg="One state value should be 15")
    self.assertAlmostEqual(states[0].probability,
                           1,
                           msg="One state probability should be 100%")
    self.assertAlmostEqual(states[0].phase,
                           0,
                           msg="One state phase should be zero")

  def test_plus_states(self):
    q1 = QUInt.pluses(4)
    states = q1.qpu.states()
    size = q1.qpu.GlobalSize()

    self.assertEqual(len(states),
                     size,
                     msg="Plus states should contain all probabilities")
    for i in range(size):
      self.assertEqual(states[i].value,
                       i,
                       msg="Plus states values should match")
      self.assertAlmostEqual(states[i].probability,
                             1 / size,
                             msg="Plus states probability should be 100%")
      self.assertAlmostEqual(states[i].phase,
                             0,
                             msg="Plus states phase should be zero")

  def test_minus_states(self):
    q1 = QUInt.minuses(4)
    states = q1.qpu.states()
    size = q1.qpu.GlobalSize()

    self.assertEqual(len(states),
                     size,
                     msg="Minus states should contain all probabilities")
    for i in range(size):
      self.assertEqual(states[i].value,
                       i,
                       msg="Minus state values should match")
      self.assertAlmostEqual(states[i].probability,
                             1 / size,
                             msg="Minus state probability should be 100%")
      self.assertAlmostEqual(states[i].phase,
                             0 if bin(i).count("1") % 2 == 0 else math.pi,
                             msg="Minus state phase should be zero")

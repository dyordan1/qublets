""" Qubit class definition """

from __future__ import annotations

from typing import TypeVar

QIntType = TypeVar("QIntType", bound="QUInt")


class Qubit:
  """ A single qubit in a Q(U)Int """

  def __init__(self, quint: QIntType, qubit: int) -> None:
    self.quint = quint
    self.qubit = qubit

  def negate(self) -> Qubit:
    """ Negates the qubit (PauliX Gate)

    Returns:
      The Qubit

    """

    self.quint.negate(self.qubit)
    return self

  def c_negate(self, on: Qubit) -> Qubit:
    """ Controlled negate on another qubit

    Returns:
      The Qubit

    """

    self.quint.c_negate(on.quint, self.qubit, on.qubit)
    return self

  def sqrt_not(self) -> Qubit:
    """ Apply square root of `not`. Applying this twice is a `not` gate

    Returns:
      The Qubit

    """

    self.quint.sqrt_not(self.qubit)
    return self

  def hadamard(self) -> Qubit:
    """ Applies a hadamard gate. Puts the qubit in an exact superposition

    Returns:
      The Qubit

    """

    self.quint.hadamard(self.qubit)
    return self

  def dburby(self) -> Qubit:
    """ An alias for hadamard

    Returns:
      The Qubit

    """

    return self.hadamard()

  def swap(self, other: Qubit) -> Qubit:
    """ Swap with a give qubit

    Args:
      other: Qubit to swap with

    Returns:
      The original Qubit method was called on

    """

    self.quint.swap(other.quint, self.qubit, other.qubit)
    return self

  def c_swap(self, other: Qubit, on: Qubit) -> Qubit:
    self.quint.c_swap(other.quint, self.qubit, other.qubit, on=on)
    return self

  def measure(self) -> int:
    return self.quint.measure(self.qubit)

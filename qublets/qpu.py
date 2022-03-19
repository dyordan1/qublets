""" QPU class definition """

from .iqs import _iqs


class QPU(_iqs.QubitRegister):
  """ Utility class to represent a QPU that can be split up into Q(U)Ints

  Args:
    num_qubits: How many qubits to allocated to the QPU

  """

  def __init__(self, num_qubits: int) -> None:
    self.num_qubits = num_qubits
    self._next_qubit = 0
    super().__init__(num_qubits, "base", 0, 0)

  def _reserve(self, num_qubits: int):
    if self._next_qubit + num_qubits > self.num_qubits:
      raise Exception(
          "Overcommitted QPU! You tried to reserve more qubits than available!")

    self._next_qubit += num_qubits

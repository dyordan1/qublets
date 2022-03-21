""" Swap test demo """

from qublets import QPU, QUInt, Simulation

# Change the values here - the likelihood of swap test to return 1 should go
# down to 50% for opposite values - and anywhere between 50% and 100% for
# "close" positions - e.g. try a superposition
first_value = 0
second_value = 0


def work():
  qpu = QPU(3)
  q1 = QUInt.value(1, first_value, qpu=qpu)
  q2 = QUInt.value(1, second_value, qpu=qpu)
  ancilla = QUInt.zeros(1, qpu=qpu)
  # There's a shortcut in the API already...
  # res = q1.swap_test(q2, on=ancilla[0])
  # But let's derive it:
  q1.c_swap(q2, on=ancilla[0].h())
  return ancilla.h().negate().measure()


sim = Simulation(1000, work)
print(sim.run())

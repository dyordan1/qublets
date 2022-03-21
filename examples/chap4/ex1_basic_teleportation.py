""" Basic Teleportation """

from math import pi
from time import sleep
from typing import Tuple
from qublets import QUInt, QPU

# The number of bits to teleport. 8 is where most classical CPUs catch on fire.
teleportation_size = 4
# The payload data to teleport - make sure it fits in number of bits above.
payload_data = 7
# Whether or not to "quantumize" the payload. If set, the payload data above is
# applied quantum operations to demonstrate *exact* quantum state is teleported,
# not just classical data (which would be a bit unexciting). However -
# quantimizing the payload adds errors :)
# So we have it off by default for the huzzah moment of 100% reliability.
quantumize_payload = False


class Teleporter:
  """
  Teleporter helper class. The general gist is:
  * `make_pair` of teleporting QUInts of matching size
  * `send` using your quantum payload and the pair
  * `receive` the quantum payload using classical data from send and the pair
  """

  def __init__(self, qpu: QPU):
    self.qpu = qpu
    self.initialized = False
    self.size = None

  def make_pair(self, size: int) -> Tuple[QUInt, QUInt]:
    """ Makes a new pre-tangled pair to use for teleportation. """
    if self.initialized:
      raise Exception(
          "Sorry, this is the store-brand teleporter that can only manage one "
          "pair at a time - feel free to modify it!")

    # Just a classic Hadamard / CNOT circuit...
    # TODO(dyordan1): Do we want c_negate(on: QUInt) in the API? Could be
    # messy with an existing c_negate(on: Qubit).
    self.first = QUInt.pluses(size, qpu=self.qpu)
    self.second = QUInt.zeros(size, qpu=self.qpu)
    for i in range(size):
      self.second[i].c_negate(on=self.first[i])

    # Reserve a scratch int for receiving
    self.scratch = QUInt.zeros(size, qpu=self.qpu)
    self.initialized = True
    self.size = size
    return (self.first, self.second)

  def send(self, data: QUInt) -> Tuple[int, int]:
    """ Send a qubit across an already pre-tangled pair. """
    if data.num_qubits != self.size:
      raise Exception(f"Sorry, can only teleport exactly {self.size} qubits!")

    # Entangle all qubits of first in pair with the payload.
    # TODO(dyordan1): Do we want c_negate(on: QUInt) in the API? Could be
    # messy with an existing c_negate(on: Qubit).
    for i in range(self.size):
      self.first[i].c_negate(on=data[i])

    # Hadamard before read ensures a fully entangled (and thus teleported) state
    data.h()

    # Collapse and return payload and first in pair
    return (data.measure(), self.first.measure())

  def receive(self, classical_results: Tuple[int, int]) -> QUInt:
    """ Receive a qubit from a pre-tangled pair using send results. """
    max_value = (1 << self.size) - 1
    if classical_results[0] > max_value:
      raise Exception(
          f"Hm... this doesn't look like data from teleporting {self.size} "
          "qubits...")

    # Set the scratch QUInts to the classical results.
    # We're reusing the first QUInt since it's already collapsed, but in a real
    # teleportation we'd have two scratch QUInts to operate with, in addition to
    # the pre-tangled second qubit.
    self.scratch.set(classical_results[0])
    self.first.set(classical_results[1])

    # To read the data, simply apply a CNOT and CPHASE based on the data.
    for i in range(self.size):
      self.second[i].c_negate(on=self.first[i])
      self.second[i].c_phase(on=self.scratch[i])

    return self.second


# Initialize - QPU needs to accomodate 4 QUInts:
# payload, entangled pair (2), scratch for receiving
main_qpu = QPU(teleportation_size * 4)
teleporter = Teleporter(main_qpu)

# Generate a teleporting pair for 1 qubit (make sure QPU has enough capacity
# for the 2 new QUInts)
pair = teleporter.make_pair(teleportation_size)

# Theoretically, Alice and Bob now take each of those QUInts and go on opposite
# sides of the galaxy... Once there, Alice generates her payload.
print(f"Alice is making a payload with data {payload_data}...")
payload = QUInt.value(teleportation_size, payload_data, qpu=main_qpu)
if quantumize_payload:
  payload = payload.h().phase(angle=-pi / 4).h()

print("Alice is sending payload to Bob...")
send_results = teleporter.send(payload)

# This is where the classical bits will be relayed over to Bob...
# We'll be cheeky and add a sleep. Feel free to remove.
print("Alice is relaying classical results to Bob...")
sleep(1.5)

print("Bob is attempting to read teleported data...")
received = teleporter.receive(send_results)

# If we quantumized the payload, let's undo those actions to see if it worked
if quantumize_payload:
  received = received.h().phase(angle=pi / 4).h()

# Hopefully, this is the same as the original payload :)
measured_received = received.measure()
print(f"Bob received {measured_received}!")

if measured_received == payload_data:
  print("Teleportation successful!")
else:
  print("Teleportation failed :(")

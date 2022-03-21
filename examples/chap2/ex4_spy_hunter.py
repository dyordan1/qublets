""" Spy Hunter Example """

from qublets import QPU, QUInt

# Change configuration to test the outcome
spy_is_present = True

# Initialize
qpu = QPU(3)
alice = QUInt.zeros(1, qpu=qpu)
fiber = QUInt.zeros(1, qpu=qpu)
bob = QUInt.zeros(1, qpu=qpu)


def random_bool(qubit):
  return bool(qubit.set(0).h().measure())


# Generate perfect random for set_value and use_had
send_one = random_bool(alice)
use_had_send = random_bool(alice)
print(f"Send 1: {send_one}")
print(f"Use Hadamard on send: {use_had_send}")

# Prepare Alice's qubit
alice.set(0)
if send_one:
  alice.negate()

if use_had_send:
  alice.h()

# "Send" the qubit
alice.swap(fiber)

# Spy on the signal
if spy_is_present:
  spied_val = fiber.h().measure()
  print(f"Spy saw: {spied_val}")
  fiber.set(0)
  if spied_val == 1:
    fiber.negate()
  fiber.h()

# "Receive" the qubit
fiber.swap(bob)

# Ingest the signal
use_had_receive = random_bool(bob)
print(f"Use Hadamard on receive: {use_had_receive}")
if use_had_receive:
  bob.h()
received = bob.measure()

if use_had_send == use_had_receive:
  if send_one == bool(received):
    print("Caught a spy!")

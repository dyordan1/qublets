Qublet Examples
===

To run any of the examples below, simply replace the body of the function called `work` in the stanza below:
```python
from qublets import QInt, QUInt

def work():
  return QInt.zeros(0).measure()

sim = Simulation(1000, work)
print(sim.run())
print(f"Took {sim.last_time}ms")
```

Uniform random distribution on 4-bit signed integer
---
```python
def work():
  return QInt.pluses(4).measure()

# Example Output: [(-8, 62), (-7, 58), (-6, 61), (-5, 66), (-4, 69), (-3, 66), (-2, 67), (-1, 75), (0, 60), (1, 54), (2, 73), (3, 54), (4, 57), (5, 49), (6, 64), (7, 65)]
# Took 131.73ms
```

Fully entangled 4-bit unsigned integer
---
```python
def work():
  return QUInt.fully_entangled(4).measure()

# Example Output: [(-1, 461), (0, 539)]
# Took 125.48ms

```

Swapping 4-bit integers on a shared QPU
---
```python
def work():
  qpu = QPU(8)
  first = QUInt.fully_entangled(4, qpu)
  second = QUInt.pluses(4, qpu)
  first.swap(second)
  return first.measure()

# Example Output: [(0, 63), (1, 68), (2, 72), (3, 50), (4, 51), (5, 57), (6, 66), (7, 54), (8, 67), (9, 66), (10, 64), (11, 65), (12, 57), (13, 70), (14, 69), (15, 61)]
# Took 972.47ms
```

Conditionally swapping 4-bit integers (superposition ancilla)
---
```python
def work():
  qpu = QPU(9)
  first = QUInt.fully_entangled(4, qpu)
  second = QUInt.pluses(4, qpu)

  # Ancilla is in a superposition, so we'd expect about half to be swapped...
  ancilla = QUInt.pluses(1, qpu)[0]
  first.c_swap(second, on=ancilla)
  return first.measure()

# Example Output: [(0, 247), (1, 28), (2, 39), (3, 27), (4, 21), (5, 49), (6, 31), (7, 28), (8, 31), (9, 41), (10, 31), (11, 23), (12, 44), (13, 36), (14, 31), (15, 293)]
# Took 4603.11ms
```

Swap Test
---
```python
def work():
  qpu = QPU(9)
  # We'd expect a 50/50 result on swap test since the quints are not equal.
  # You should get only 1s for the ancilla readout if you set them to be.
  first = QUInt.zeros(4, qpu)
  second = QUInt.ones(4, qpu)

  # Ancilla state doesn't matter, it gets trampled
  ancilla = QUInt.pluses(1, qpu)[0]
  return first.swap_test(second, on=ancilla)

# Example Output: [(0, 547), (1, 453)]
# Took 5304.76ms
```
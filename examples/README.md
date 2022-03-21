Book Examples
===

All the examples in this folder are a re-implementations of the examples in the "Programming Quantum Computers" by Eric R. Johnston, Nic Harrigan & Mercedes Gimeno-Segovia, published by O'Reilly \[[ISBN-13: 978-1492039686](https://www.amazon.com/Programming-Quantum-Computers-Essential-Algorithms/dp/1492039683)\]. You can find the web QCEngine written by the authors [here](https://oreilly-qc.github.io/#). It is, quite expectedly, capable of running all of the examples as well. You can also find all the JS code samples in the authors' [GitHub repository](https://github.com/oreilly-qc/oreilly-qc.github.io).

The book is an amazingly approachable introduction to quantum computing, written as a practical guide for programmers. Whether or not you have experience with quantum, it's a wonderful read and highly recommended by the qublets author :)

Running the Examples
---

Make sure you have qublets installed before attempting to run the examples - they all import `qublets` from global.

```bash
pip install qublets
python3 examples/chap2/ex1_random_bit.py
```

***Note**: If you want to iterate on the qublets engine while running the examples, you can add the qublets namespace to global using `sys.path.insert(0, path_to_qublets)` instead. You will have to compile `intel-qc` from source and all the other good stuff, check out [`build_from_source.md`](../build_from_source.md) for more info.*
import numpy as np
import pennylane as qml

### challenge 1
n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)

@qml.qnode(dev)
def naive_circuit():
    """Create a uniform superposition and return the probabilities.

    Returns: 
        array[float]: Probabilities for observing different outcomes.
    """
    for wire in range(n_bits):

        qml.Hadamard(wires=wire)

    return qml.probs(wires=range(n_bits))

print("---\nchallenge 1")
print(naive_circuit())

### challenge 2

print("---\nchallenge 2")
print("empty challenge")
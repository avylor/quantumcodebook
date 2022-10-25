import numpy as np
import pennylane as qml

### challenge 1
def oracle_matrix(combo):
    """Return the oracle matrix for a secret combination.
    
    Args:
        combo (list[int]): A list of bits representing a secret combination.
         
    Returns: 
        array[float]: The matrix representation of the oracle.
    """
    index = np.ravel_multi_index(combo, [2]*len(combo)) # Index of solution
    my_array = np.identity(2**len(combo)) # Create the identity matrix
    my_array[index, index] = -1
    return my_array

n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)

@qml.qnode(dev)
def hoh_circuit(combo):
    """A circuit which applies Hadamard-oracle-Hadamard and returns probabilities.
    
    Args:
        combo (list[int]): A list of bits representing a secret combination.

    Returns:
        list[float]: Measurement outcome probabilities.
    """

    qml.broadcast(qml.Hadamard, wires=range(n_bits), pattern="single")
    qml.QubitUnitary(oracle_matrix(combo), wires=range(len(combo)))
    qml.broadcast(qml.Hadamard, wires=range(n_bits), pattern="single")

    return qml.probs(wires=range(n_bits))

print("---\nchallenge 1")
print(hoh_circuit([0,0,0,0]))

### challenge 2

print("---\nchallenge 2")
print("empty challenge")

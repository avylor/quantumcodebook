import numpy as np
import pennylane as qml

### challenge 1
n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)

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

@qml.qnode(dev)
def oracle_amp(combo):
    """Prepare the uniform superposition and apply the oracle.

    Args:
        combo (list[int]): A list of bits representing the secret combination.

    Returns: 
        array[complex]: The quantum state (amplitudes) after applying the oracle.
    """
    qml.broadcast(qml.Hadamard, wires=range(n_bits), pattern="single")
    qml.QubitUnitary(oracle_matrix(combo),wires=range(n_bits))
    return qml.state()

print("---\nchallenge 1")
print(oracle_amp([0,1,0,1]))

### challenge 2
n_bits = 4

def diffusion_matrix():
    """Return the diffusion matrix.

    Returns: 
        array[float]: The matrix representation of the diffusion operator.
    """
    matrix = 1/(2**(n_bits-1))*np.ones((2**n_bits, 2**n_bits)) - np.eye(2**n_bits)
    return matrix

@qml.qnode(dev)
def difforacle_amp(combo):
    """Apply the oracle and diffusion matrix to the uniform superposition.

    Args:
        combo (list[int]): A list of bits representing the secret combination.

    Returns:
        array[complex]: The quantum state (amplitudes) after applying the oracle
        and diffusion.
    """
    qml.broadcast(qml.Hadamard, wires=range(n_bits), pattern="single")
    qml.QubitUnitary(oracle_matrix(combo),wires=range(n_bits))
    qml.QubitUnitary(diffusion_matrix(),wires=range(n_bits))
    return qml.state()

print("---\nchallenge 2")
print(difforacle_amp([0,1,0,1]))

### challenge 3
@qml.qnode(dev)
def two_difforacle_amp(combo):
    """Apply the Grover operator twice to the uniform superposition.

    Args:
        combo (list[int]): A list of bits representing the secret combination.

    Returns: 
        array[complex]: The resulting quantum state.
    """
    qml.broadcast(qml.Hadamard, wires=range(n_bits), pattern="single")
    for i in range(2):
        qml.QubitUnitary(oracle_matrix(combo),wires=range(n_bits))
        qml.QubitUnitary(diffusion_matrix(),wires=range(n_bits))

    return qml.state()

print("---\nchallenge 3")
print(two_difforacle_amp([0,1,0,1]))

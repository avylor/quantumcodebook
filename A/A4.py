import numpy as np
import pennylane as qml


### challenge 1
n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)

def multisol_oracle_matrix(combos):
    """Return the oracle matrix for a set of solutions.

    Args:
        combos (list[list[int]]): A list of secret bit strings.

    Returns:
        array[float]: The matrix representation of the oracle.
    """
    my_array = np.identity(2**n_bits)

    indices = [np.ravel_multi_index(combo, [2]*len(combo)) for combo in combos]
    for index in indices:
        my_array[index, index] = -1

    return my_array


@qml.qnode(dev)
def multisol_pair_circuit(x_tilde, combos):
    """Implements the circuit for testing a pair of combinations labelled by x_tilde.
    
    Args:
        x_tilde (list[int]): An (n_bits - 1)-bit string labelling the pair to test.
        combos (list[list[int]]): A list of secret bit strings.

    Returns:
        array[float]: Probabilities on the last qubit.
    """
    for i in range(n_bits-1): # Initialize x_tilde part of state
        if x_tilde[i] == 1:
            qml.PauliX(wires=i)

    qml.Hadamard(wires=n_bits-1)
    qml.QubitUnitary(multisol_oracle_matrix(combos), wires=range(n_bits))
    qml.Hadamard(wires=n_bits-1)

    return qml.probs(wires=n_bits-1)

print("---\nchallenge 1")
print(multisol_pair_circuit([0,0,0], [[0,0,0,0]]))


### challenge 2
def parity_checker(combos):
    """Use multisol_pair_circuit to determine the parity of a solution set.

    Args:
        combos (list[list[int]]): A list of secret combinations.

    Returns: 
        int: The parity of the solution set.
    """
    parity = 0
    x_tilde_strs = [np.binary_repr(n, n_bits-1) for n in range(2**(n_bits-1))]
    x_tildes = [[int(s) for s in x_tilde_str] for x_tilde_str in x_tilde_strs]
    for x_tilde in x_tildes:

        probs = multisol_pair_circuit(x_tilde, combos)
        if np.isclose(probs[1], 1.):
            parity += 1
    parity = parity % 2
    return parity

print("---\nchallenge 2")
print(parity_checker([[0,0,0,0]]))


### challenge 3

print("---\nchallenge 3")
print("empty challenge")

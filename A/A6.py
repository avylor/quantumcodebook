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
def multisol_hoh_circuit(combos):
    """A circuit which applies Hadamard, multi-solution oracle, then Hadamard.
    
    Args:
        combos (list[list[int]]): A list of secret bit strings.

    Returns: 
        array[float]: Probabilities for observing different outcomes.
    """

    qml.broadcast(qml.Hadamard, wires=range(n_bits), pattern="single")
    qml.QubitUnitary(multisol_oracle_matrix(combos), wires=range(n_bits))
    qml.broadcast(qml.Hadamard, wires=range(n_bits), pattern="single")

    return qml.probs(wires=range(n_bits))

print("---\nchallenge 1")
print(multisol_hoh_circuit([[0,0,0,0], [0,0,0,1]]))


### challenge 2
def deutsch_jozsa(promise_var):
    """Implement the Deutsch-Jozsa algorithm and guess the promise variable.
    
    Args:
        promise_var (int): Indicates whether the function is balanced (0) or constant (1).
        
    Returns: 
        int: A guess at the promise variable.
    """
    if promise_var == 0:
        how_many = 2**(n_bits - 1)
    else:
        how_many = np.random.choice([0, 2**n_bits]) # Choose all or nothing randomly
    combos = []
    # combos = multisol_combo(n_bits, how_many) # Generate random combinations # TODO uncomment for submission
    probs = multisol_hoh_circuit(combos)
    if np.isclose(probs[0], 1.):
        return 1
    else:
        return 0

print("---\nchallenge 2")
print(deutsch_jozsa(1))

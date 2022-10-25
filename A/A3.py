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
def pair_circuit(x_tilde, combo):
    """Test a pair labelled by x_tilde for the presence of a solution.
    
    Args:
        x_tilde (list[int]): An (n_bits - 1)-string labelling the pair to test.
        combo (list[int]): A secret combination of n_bits 0s and 1s.
        
    Returns:
        array[float]: Probabilities on the last qubit.
    """
    for i in range(n_bits-1): # Initialize x_tilde part of state
        if x_tilde[i] == 1:
            qml.PauliX(wires=i)

    qml.Hadamard(n_bits-1)
    qml.QubitUnitary(oracle_matrix(combo), wires=range(n_bits))
    qml.Hadamard(n_bits-1)
    
    return qml.probs(wires=n_bits-1)

print("---\nchallenge 1")
print(pair_circuit([0,0,0], [0,0,0,0]))

### challenge 2
def pair_lock_picker(trials):
    """Create a combo, run pair_circuit until it succeeds, and tally success rate.
    
    Args:
        trials (int): Number of times to test the lock picker.

    Returns:
        float: The average number of times the lock picker uses pair_circuit.
    """
    x_tilde_strs = [np.binary_repr(n, n_bits-1) for n in range(2**(n_bits-1))]
    x_tildes = [[int(s) for s in x_tilde_str] for x_tilde_str in x_tilde_strs] 

    test_numbers = []

    for trial in range(trials):
        combo = [0,0,1,0]
        # combo = secret_combo(n_bits) # Random list of bits # TODO uncomment for submission
        counter = 0
        for x_tilde in x_tildes:
            counter += 1

            probs = pair_circuit(x_tilde, combo)
            if np.isclose(probs[1], 1.):
                break
        
        test_numbers.append(counter)
    return sum(test_numbers)/trials

trials = 500
output = pair_lock_picker(trials)

print("---\nchallenge 2")
print(f"For {n_bits} bits, it takes", output, "pair tests on average.")

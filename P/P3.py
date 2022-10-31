import numpy as np
import pennylane as qml

### challenge 1
dev = qml.device("default.qubit", wires=10)

def fractional_binary_to_decimal(binary_fraction, wires):
    return float(binary_fraction/ 2 ** len(wires))

def phase_window(probs, estimation_wires):
    """ Given an array of probabilities, return the phase window of the unitary's eigenvalue
    
    Args: 
        probs (array[float]): Probabilities on the estimation wires.
        estimation_wires (list[int]): List of estimation wires
    
    Returns:
        (float, float): the lower and upper bound of the phase
    """

    max_ind = np.argmax(probs)
    bound_1 = fractional_binary_to_decimal(max_ind, estimation_wires) # MOST LIKELY OUTCOME
    tmp_prob = probs[max_ind]
    probs[max_ind] = 0.
    bound_2 = fractional_binary_to_decimal(np.argmax(probs), estimation_wires)# SECOND MOST LIKELY OUTCOME
    probs[max_ind] = tmp_prob
    return bound_2, bound_1

# You can increase the number of estimation wires to a maximum of range(0, 9)
estimation_wires = range(0, 9)

# The target is set to the last qubit
target_wires = [9]

# Define the unitary
U = np.array([[1, 0], [0, np.exp((2*np.pi*1j/7))]])

# probs = qpe(U, estimation_wires, target_wires)

# MODIFY TO TRUE AFTER TESTING YOUR SOLUTION
done = True
print("---\nchallenge 1")


### challenge 2
dev = qml.device("default.qubit", wires=10)

def estimates_array(unitary):
    """ Given a unitary, return a list of its phase windows
    
    Args: 
        unitary (array[complex]): A unitary matrix.
    
    Returns:
        [(float, float)]: a list of phase windows for 1 to 9 
        estimation wires
    """

    estimates = []
    target_wires = [9]

    for nr_wires in range(2,10):
        #probs = qpe(unitary, range(nr_wires), target_wires) # TODO uncomment for submission
        #estimates.append(phase_window(probs, range(nr_wires))) #TODO uncomment for submission
        pass

    return estimates

# Define the unitary
U = np.array([[1, 0], [0, np.exp((2*np.pi*1j/7))]])

estimates_array(U)

print("---\nchallenge 2")



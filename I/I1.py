import numpy as np


### challenge 1
ket_0 = np.array([1, 0])
ket_1 = np.array([0, 1])

def normalize_state(alpha, beta):
    """Compute a normalized quantum state given arbitrary amplitudes.
    
    Args:
        alpha (complex): The amplitude associated with the |0> state.
        beta (complex): The amplitude associated with the |1> state.
        
    Returns:
        array[complex]: A vector (numpy array) with 2 elements that represents
        a normalized quantum state.
    """
    
    return np.array([alpha/np.sqrt(alpha*alpha + beta*beta), beta/np.sqrt(alpha*alpha + beta*beta)])

print("---\nchallenge 1")
print(normalize_state(complex(1,1), complex(2,2)))
print(np.linalg.norm(normalize_state(complex(1,1), complex(2,2))))


### challenge 2
def inner_product(state_1, state_2):
    """Compute the inner product between two states.
    
    Args:
        state_1 (array[complex]): A normalized quantum state vector
        state_2 (array[complex]): A second normalized quantum state vector
        
    Returns:
        complex: The value of the inner product <state_1 | state_2>.
    """

    return np.sum(state_1*np.conjugate(state_2))


# Test your results with this code
ket_0 = np.array([1, 0])
ket_1 = np.array([0, 1])

print("---\nchallenge 2")
print(f"<0|0> = {inner_product(ket_0, ket_0)}")
print(f"<0|1> = {inner_product(ket_0, ket_1)}")
print(f"<1|0> = {inner_product(ket_1, ket_0)}")
print(f"<1|1> = {inner_product(ket_1, ket_1)}")


### challenge 3
def measure_state(state, num_meas):
    """Simulate a quantum measurement process.

    Args:
        state (array[complex]): A normalized qubit state vector. 
        num_meas (int): The number of measurements to take
        
    Returns:
        array[int]: A set of num_meas samples, 0 or 1, chosen according to the probability 
        distribution defined by the input state.
    """

    prob_1 = np.absolute(state[1])**2
    rng = np.random.default_rng()
    return rng.binomial(1, prob_1, num_meas)

print("---\nchallenge 3")
print(measure_state(np.array([np.sqrt(0.75), complex(0, 0.5)]), 10))


### challenge 4
U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

def apply_u(state):
    """Apply a quantum operation.

    Args:
        state (array[complex]): A normalized quantum state vector. 
        
    Returns:
        array[complex]: The output state after applying U.
    """

    return np.matmul(U, state)

print("---\nchallenge 4")
print(apply_u(np.array([np.sqrt(0.75), complex(0, 0.5)])))


### challenge 5
U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

def initialize_state():
    """Prepare a qubit in state |0>.
    
    Returns:
        array[float]: the vector representation of state |0>.
    """

    return np.array([1.0, 0.0])

def apply_u(state):
    """Apply a quantum operation."""

    return np.dot(U, state)


def measure_state(state, num_meas):
    """Measure a quantum state num_meas times."""
    p_alpha = np.abs(state[0]) ** 2
    p_beta = np.abs(state[1]) ** 2
    meas_outcome = np.random.choice([0, 1], p=[p_alpha, p_beta], size=num_meas)

    return meas_outcome


def quantum_algorithm():
    """Use the functions above to implement the quantum algorithm described above.
    
    Try and do so using three lines of code or less!
    
    Returns:
        array[int]: the measurement results after running the algorithm 100 times
    """

    state = initialize_state()
    transformed_state = apply_u(state)
    return measure_state(transformed_state, 100)

print("---\nchallenge 5")
print(quantum_algorithm())
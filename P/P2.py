import numpy as np
import pennylane as qml

### challenge 1
def U_power_2k(unitary, k):
    """ Computes U at a power of 2k (U^2^k)
    
    Args: 
        unitary (array[complex]): A unitary matrix
    
    Returns: 
        array[complex]: the unitary raised to the power of 2^k
    """
    return np.linalg.matrix_power(unitary, 2**k)
            

# Try out a higher power of U
U = qml.T.compute_matrix()

print("---\nchallenge 1")
print(U)
print(U_power_2k(U, 2))


### challenge 2
estimation_wires = [0, 1, 2]
target_wires = [3]

def apply_controlled_powers_of_U(unitary):
    """A quantum function that applies the sequence of powers of U^2^k to
    the estimation wires.
    
    Args: 
        unitary (array [complex]): A unitary matrix
    """

    for ind, e_wire in enumerate(estimation_wires):
        qml.ControlledQubitUnitary(U_power_2k(unitary, len(estimation_wires)-ind-1), control_wires=e_wire, wires=target_wires)

print("---\nchallenge 2")


### challenge 3
dev = qml.device("default.qubit", wires=4)

estimation_wires = [0, 1, 2]
target_wires = [3]

def prepare_eigenvector():
    qml.PauliX(wires=target_wires)

@qml.qnode(dev)
def qpe(unitary):
    """ Estimate the phase for a given unitary.
    
    Args:
        unitary (array[complex]): A unitary matrix.
        
    Returns:
        array[float]: Measurement outcome probabilities on the estimation wires.
    """
    prepare_eigenvector()
    qml.broadcast(qml.Hadamard, pattern='single', wires=estimation_wires)
    apply_controlled_powers_of_U(unitary)
    qml.adjoint(qml.QFT(wires=estimation_wires))
    return qml.probs(wires=estimation_wires)

U = qml.T.compute_matrix()

print("---\nchallenge 3")
print(qpe(U))


### challenge 4
estimation_wires = [0, 1, 2]
target_wires = [3]

def estimate_phase(probs):
    """Estimate the value of a phase given measurement outcome probabilities
    of the QPE routine.
    
    Args: 
        probs (array[float]): Probabilities on the estimation wires.
    
    Returns:
        float: the estimated phase   
    """
    return np.argmax(probs) / 2 ** len(estimation_wires)

U = qml.T.compute_matrix()

probs = qpe(U)

estimated_phase = estimate_phase(probs)

print("---\nchallenge 4")
print(probs)
print(estimated_phase)


### challenge 5
dev = qml.device("default.qubit", wires=4)

estimation_wires = [0, 1, 2]
target_wires = [3]

def prepare_eigenvector():
    qml.PauliX(wires=target_wires)

@qml.qnode(dev)
def qpe(unitary):
    """Estimate the phase for a given unitary.
    
    Args:
        unitary (array[complex]): A unitary matrix.
        
    Returns:
        array[float]: Probabilities on the estimation wires.
    """
    
    prepare_eigenvector()
    qml.QuantumPhaseEstimation(unitary, target_wires, estimation_wires)
    return qml.probs(estimation_wires)


U = qml.T.compute_matrix()
probs = qpe(U)

print("---\nchallenge 5")
print(estimate_phase(probs))

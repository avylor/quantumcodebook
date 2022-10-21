import numpy as np
import pennylane as qml

### challenge 1
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def apply_z_to_plus():
    """Write a circuit that applies PauliZ to the |+> state and returns
    the state.

    Returns:
        array[complex]: The state of the qubit after the operations.
    """

    qml.Hadamard(wires=0)
    qml.PauliZ(wires=0)

    return qml.state()

print("---\nchallenge 1")
print(apply_z_to_plus())


### challenge 2
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def fake_z():
    """Use RZ to produce the same action as Pauli Z on the |+> state.

    Returns:
        array[complex]: The state of the qubit after the operations.
    """
    qml.Hadamard(wires=0)
    qml.RZ(phi=np.pi, wires=0)
    return qml.state()

print("---\nchallenge 2")
print(fake_z())

### challenge 3
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def many_rotations():
    """Implement the circuit depicted above and return the quantum state.

    Returns:
        array[complex]: The state of the qubit after the operations.
    """

    qml.Hadamard(wires=0)
    qml.S(wires=0)
    qml.adjoint(qml.T)(wires=0)
    qml.RZ(0.3, wires=0)
    qml.adjoint(qml.S)(wires=0)

    return qml.state()

print("---\nchallenge 3")
print(many_rotations())


### challenge 4
dev = qml.device('default.qubit', wires=3)

@qml.qnode(dev)
def too_many_ts():
    """You can implement the original circuit here as well, it may help you with
    testing to ensure that the circuits have the same effect.

    Returns:
        array[float]: The measurement outcome probabilities.
    """

    wire=0
    qml.Hadamard(wires=wire)
    qml.T(wires=wire)
    qml.T(wires=wire)
    qml.Hadamard(wires=wire)
    qml.adjoint(qml.T)(wires=wire)
    qml.adjoint(qml.T)(wires=wire)
    qml.Hadamard(wires=wire)

    wire=1
    qml.Hadamard(wires=wire)
    qml.T(wires=wire)
    qml.Hadamard(wires=wire)
    qml.T(wires=wire)
    qml.T(wires=wire)
    qml.T(wires=wire)
    qml.T(wires=wire)
    qml.Hadamard(wires=wire)

    wire=2
    qml.Hadamard(wires=wire)
    qml.adjoint(qml.T)(wires=wire)
    qml.Hadamard(wires=wire)
    qml.adjoint(qml.T)(wires=wire)
    qml.adjoint(qml.T)(wires=wire)
    qml.adjoint(qml.T)(wires=wire)
    qml.Hadamard(wires=wire)

    return qml.probs(wires=[0, 1, 2])

@qml.qnode(dev)
def just_enough_ts():
    """Implement an equivalent circuit as the above with the minimum number of 
    T and T^\dagger gates required.

    Returns:
        array[float]: The measurement outcome probabilities.
    """

    wire=0
    qml.Hadamard(wires=wire)
    qml.S(wires=wire)
    qml.Hadamard(wires=wire)
    qml.adjoint(qml.S)(wires=wire)
    qml.Hadamard(wires=wire)

    wire=1
    qml.Hadamard(wires=wire)
    qml.T(wires=wire)
    qml.Hadamard(wires=wire)
    qml.PauliZ(wires=wire)
    qml.Hadamard(wires=wire)

    wire=2
    qml.Hadamard(wires=wire)
    qml.adjoint(qml.T)(wires=wire)
    qml.Hadamard(wires=wire)
    qml.adjoint(qml.T)(wires=wire)
    qml.adjoint(qml.S)(wires=wire)
    qml.Hadamard(wires=wire)
    

    return qml.probs(wires=[0, 1, 2])

##################
# YOUR CODE HERE #
##################

# FILL IN THE CORRECT VALUES FOR THE ORIGINAL CIRCUIT
original_depth = 8
original_t_count = 13
original_t_depth = 6 # why not 5?

# FILL IN THE CORRECT VALUES FOR THE NEW, OPTIMIZED CIRCUIT
optimal_depth = 6
optimal_t_count = 3
optimal_t_depth = 2

print("---\nchallenge 4")
print(too_many_ts())
print(just_enough_ts())


### challenge 5

print("---\nchallenge 5")
print("empty challenge")
import numpy as np
import pennylane as qml

### challenge 1
def state_preparation():

    qml.Hadamard(wires=0)
    qml.Rot(0.1, 0.2, 0.3, wires=0)

print("---\nchallenge 1")


### challenge 2
dev = qml.device("default.qubit", wires=1)

def state_preparation():
    qml.Hadamard(wires=0)
    qml.Rot(0.1, 0.2, 0.3, wires=0)


@qml.qnode(dev)
def state_prep_only():
    state_preparation()
    return qml.state()

print("---\nchallenge 2")
print(state_prep_only())


### challenge 3
def entangle_qubits():
    
    # ENTANGLE THE SECOND QUBIT (WIRES=1) AND THE THIRD QUBIT
    qml.Hadamard(wires=1)
    qml.CNOT(wires=[1,2])

    
print("---\nchallenge 3")
entangle_qubits()


### challenge 4
def rotate_and_controls():

    # PERFORM THE BASIS ROTATION
    qml.CNOT(wires=[0,1])
    qml.Hadamard(wires=0)
    # PERFORM THE CONTROLLED OPERATIONS
    qml.CNOT(wires=[1,2])
    qml.CZ(wires=[0,2])

print("---\nchallenge 4")
rotate_and_controls()


### challenge 5
dev = qml.device("default.qubit", wires=3)

# OPTIONALLY UPDATE THIS STATE PREPARATION ROUTINE
def state_preparation():
    qml.Hadamard(wires=0)
    qml.Rot(0.1, 0.2, 0.3, wires=0)

@qml.qnode(dev)
def teleportation():

    state_preparation()
    entangle_qubits()
    rotate_and_controls()

    return qml.state()

print("---\nchallenge 5")
print(teleportation())

### challenge 6
def extract_qubit_state(input_state):
    """Extract the state of the third qubit from the combined state after teleportation.
    
    Args:
        input_state (array[complex]): A 3-qubit state of the form 
            (1/2)(|00> + |01> + |10> + |11>) (a|0> + b|1>)
            obtained from the teleportation protocol.
            
    Returns:
        array[complex]: The state vector np.array([a, b]) of the third qubit.
    """

    alpha = 0.5*(input_state[0]+input_state[2]+input_state[4]+input_state[6])
    beta = 0.5*(input_state[1]+input_state[3]+input_state[5]+input_state[7])

    return np.array([alpha, beta])
    

# Here is the teleportation routine for you
dev = qml.device("default.qubit", wires=3)

def state_preparation():
    qml.Hadamard(wires=0)
    qml.Rot(0.1, 0.2, 0.3, wires=0)


@qml.qnode(dev)
def teleportation():
    state_preparation()
    entangle_qubits()
    rotate_and_controls()    
    return qml.state()

# Print the extracted state after teleportation
full_state = teleportation()

print("---\nchallenge 6")
print(extract_qubit_state(full_state))


### challenge 7

print("---\nchallenge 7")
print("empty challenge")
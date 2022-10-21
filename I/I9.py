import numpy as np
import pennylane as qml

### challenge 1
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def apply_h_and_measure(state):
    """Complete the function such that we apply the Hadamard gate
    and measure in the computational basis.
    
    Args:
        state (int): Either 0 or 1. If 1, prepare the qubit in state |1>,
            otherwise leave it in state 0.
    
    Returns:
        array[float]: The measurement outcome probabilities.
    """
    if state == 1:
        qml.PauliX(wires=0)

    qml.Hadamard(wires=0)

    return qml.probs(wires=0)

print("---\nchallenge 1")
print(apply_h_and_measure(0))
print(apply_h_and_measure(1))


### challenge 2

# WRITE A QUANTUM FUNCTION THAT PREPARES (1/2)|0> + i(sqrt(3)/2)|1>
def prepare_psi():
    qml.RY(2*np.pi/3, wires=0)
    qml.RZ(np.pi/2, wires=0)

# WRITE A QUANTUM FUNCTION THAT SENDS BOTH |0> TO |y_+> and |1> TO |y_->
def y_basis_rotation():
    qml.Hadamard(wires=0)
    #qml.RZ(np.pi/2, wires=0)

print("---\nchallenge 2")
prepare_psi()
y_basis_rotation()

### challenge 3
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def measure_in_y_basis():

    prepare_psi()
    qml.adjoint(y_basis_rotation)()

    return qml.probs(wires=0)

print("---\nchallenge 3")
print(measure_in_y_basis())


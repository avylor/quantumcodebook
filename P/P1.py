import numpy as np
import pennylane as qml

### challenge 1
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def guess_the_unitary(unitary):
    """Given a unitary that performs a Z or a -Z operation
    on a qubit, guess which one it is.
    
    Args: 
        U (array[complex]): A unitary matrix, guaranteed to be either Z or -Z.
    
    Returns:
        array [int]:  Probabilities on  on the first qubit
        using qml.probs()
    """
    
    qml.Hadamard(wires=0)
    qml.ControlledQubitUnitary(unitary, control_wires=[0],wires=[1])
    qml.Hadamard(wires=0)
    return qml.probs(wires=0)

# Z gate 
U = qml.PauliZ.compute_matrix() 

# -Z gate
U = (-1)*qml.PauliZ.compute_matrix()

print("---\nchallenge 1")
print(guess_the_unitary(U))


### challenge 2
dev = qml.device("default.qubit", wires=2)
        
@qml.qnode(dev)
def phase_kickback_X(eigenvector):
    """ Given an eigenvector of X, 
    apply the phase kickback circuit to observe 
    the probabilities on the control wire
    
    Args: 
        eigenvector(String): A string "plus" or "minus" depicting 
        the eigenvector of X
    
    Returns:
        array[int]: Measurement outcome on the first qubit using qml.probs()
    """
    # Prepare |ψ>
    if eigenvector == "plus":
        qml.Hadamard(wires=1)
    else:
        qml.PauliX(wires=1)
        qml.Hadamard(wires=1)
    
    # Phase kickback
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0,1])
    qml.Hadamard(wires=0)
 
    return qml.probs(wires=[0])   

# MODIFY EIGENVALUES BELOW 
eigenvalue_of_X_plus = 1
eigenvalue_of_X_minus = -1

print("---\nchallenge 2")
print(phase_kickback_X("plus"))
print(phase_kickback_X("minus"))

### challenge 3

print("---\nchallenge 3")
print("empty challenge")


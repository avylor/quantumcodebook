import numpy as np
import pennylane as qml

### challenge 1
dev = qml.device("default.qubit", wires=1)

phi, theta, omega = np.pi/2, np.pi/2, np.pi/2

@qml.qnode(dev)
def hadamard_with_rz_rx():
    qml.RZ(phi, wires=0)
    qml.RX(theta, wires=0)
    qml.RZ(omega, wires=0)
    return qml.state()


print("---\nchallenge 1")
print(hadamard_with_rz_rx())


### challenge 2
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def convert_to_rz_rx():
    """
    qml.RZ(np.pi/2, wires=0)
    qml.RX(np.pi/2, wires=0)
    qml.RZ(np.pi/2, wires=0)
    qml.RZ(np.pi/2, wires=0)
    qml.RZ(-np.pi/4, wires=0)
    qml.RZ(np.pi/2, wires=0)
    qml.RX(np.pi, wires=0)
    qml.RZ(-np.pi/2, wires=0)
    """
    qml.RZ(np.pi/2, wires=0)
    qml.RX(np.pi/2, wires=0)
    qml.RZ(1.5*np.pi - np.pi/4, wires=0)
    qml.RX(np.pi, wires=0)
    qml.RZ(-np.pi/2, wires=0)
    return qml.state()

print("---\nchallenge 2")
print(convert_to_rz_rx())

### challenge 3

dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def unitary_with_h_and_t():
    
    qml.Hadamard(wires=0)
    qml.T(wires=0)
    qml.Hadamard(wires=0)
    qml.T(wires=0)
    qml.T(wires=0)
    qml.Hadamard(wires=0)

    return qml.state()

print("---\nchallenge 3")
print(unitary_with_h_and_t())

### challenge 4

print("---\nchallenge 4")
print("empty challenge")
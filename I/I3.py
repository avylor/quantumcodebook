import numpy as np
import pennylane as qml

### challenge 1
dev = qml.device("default.qubit", wires=1)

U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

@qml.qnode(dev)
def apply_u():

    qml.QubitUnitary(U, wires=0)
    return qml.state()

print("---\nchallenge 1")
print(apply_u())

### challenge 2
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def apply_u_as_rot(phi, theta, omega):

    qml.Rot(phi, theta, omega, wires=0)

    return qml.state()

print("---\nchallenge 2")
print(apply_u_as_rot(0.1, 0.1, 0.1))

### challenge 3

print("---\nchallenge 3")
print("no challenge")

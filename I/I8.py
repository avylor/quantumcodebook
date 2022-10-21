import numpy as np
import pennylane as qml

### challenge 1
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def prepare_state():
    qml.Hadamard(wires=0)
    qml.RZ(5*np.pi/4, wires=0)

    return qml.state()

print("---\nchallenge 1")
print(prepare_state())


### challenge 2
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def prepare_state():
    qml.RX(np.pi/3, wires=0)

    return qml.state()

print("---\nchallenge 2")
print(prepare_state())


### challenge 3
v = np.array([0.52889389-0.14956775j, 0.67262317+0.49545818j])

dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def prepare_state(state=v):
    qml.MottonenStatePreparation(state, wires=0)
    return qml.state()

# This will draw the quantum circuit and allow you to inspect the output gates
print("---\nchallenge 3")
print(prepare_state(v))
print()
print(qml.draw(prepare_state)(v))



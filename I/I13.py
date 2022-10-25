import numpy as np
import pennylane as qml

### challenge 1
dev = qml.device("default.qubit", wires=2)

# Prepare a two-qubit state; change up the angles if you like
phi, theta, omega = 1.2, 2.3, 3.4


@qml.qnode(device=dev)
def true_cz(phi, theta, omega):
    # prepare_states(phi, theta, omega) # TODO uncomment for submission
    qml.CZ(wires=[0,1])
    
    return qml.state()


@qml.qnode(dev)
def imposter_cz(phi, theta, omega):
    # prepare_states(phi, theta, omega) # TODO uncomment for submission
    qml.Hadamard(wires=1)
    qml.CNOT(wires=[0,1])
    qml.Hadamard(wires=1)
    
    return qml.state()


print("---\nchallenge 1")
print(f"True CZ output state {true_cz(phi, theta, omega)}")
print(f"Imposter CZ output state {imposter_cz(phi, theta, omega)}")


### challenge 2
dev = qml.device("default.qubit", wires=2)

# Prepare a two-qubit state; change up the angles if you like
phi, theta, omega = 1.2, 2.3, 3.4

@qml.qnode(dev)
def apply_swap(phi, theta, omega):
    # prepare_states(phi, theta, omega) # TODO uncomment for submission

    qml.SWAP(wires=[0,1])

    return qml.state()


@qml.qnode(dev)
def apply_swap_with_cnots(phi, theta, omega):
    # prepare_states(phi, theta, omega) # TODO uncomment for submission
    
    qml.CNOT(wires=[0,1])
    qml.CNOT(wires=[1,0])
    qml.CNOT(wires=[0,1])

    return qml.state()

print("---\nchallenge 2")
print(f"Regular SWAP state = {apply_swap(phi, theta, omega)}")
print(f"CNOT SWAP state = {apply_swap_with_cnots(phi, theta, omega)}")


### challenge 3
dev = qml.device("default.qubit", wires=3)

# Prepare first qubit in |1>, and arbitrary states on the second two qubits
phi, theta, omega = 1.2, 2.3, 3.4


# A helper function just so you can visualize the initial state
# before the controlled SWAP occurs.
@qml.qnode(dev)
def no_swap(phi, theta, omega):
    # prepare_states(phi, theta, omega) # TODO uncomment for submission
    return qml.state()


@qml.qnode(dev)
def controlled_swap(phi, theta, omega):
    # prepare_states(phi, theta, omega) # TODO uncomment for submission
    
    qml.Toffoli(wires=[0,1,2])
    qml.Toffoli(wires=[0,2,1])
    qml.Toffoli(wires=[0,1,2])

    return qml.state()

print("---\nchallenge 3")

print(no_swap(phi, theta, omega))
print(controlled_swap(phi, theta, omega))


### challenge 4
dev = qml.device('default.qubit', wires=4)

@qml.qnode(dev)
def four_qubit_mcx():
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)
    qml.MultiControlledX(wires=[0,1,2,3], control_values="001")

    return qml.state()

print("---\nchallenge 4")
print(four_qubit_mcx())


### challenge 5
# Wires 0, 1, 2 are the control qubits
# Wire 3 is the auxiliary qubit
# Wire 4 is the target 
dev = qml.device('default.qubit', wires=5)


@qml.qnode(dev)
def four_qubit_mcx_only_tofs():
    # We will initialize the control qubits in state |1> so you can see
    # how the output state gets changed.
    qml.PauliX(wires=0)
    qml.PauliX(wires=1)
    qml.PauliX(wires=2)

    qml.Toffoli(wires=[0,1,3])
    qml.Toffoli(wires=[2,3,4])
    qml.Toffoli(wires=[0,1,3])

    return qml.state()

print("---\nchallenge 5")
print(four_qubit_mcx_only_tofs())


### challenge 6

print("---\nchallenge 6")
print("empty challenge")
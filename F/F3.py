import numpy as np
import pennylane as qml

### challenge 1
dev = qml.device("default.qubit", wires=3)

@qml.qnode(dev)
def three_qubit_QFT(basis_id):
    """A circuit that computes the QFT on three qubits.
    
    Args:
        basis_id (int): An integer value identifying the basis state to construct.
        
    Returns:
        array[complex]: The state of the qubits after the QFT operation.
    """
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=dev.num_wires)]
    qml.BasisStatePreparation(bits, wires=[0, 1, 2])
    
    qml.Hadamard(wires=0)
    qml.ctrl(qml.S, control=1)(wires=0)
    qml.ctrl(qml.T, control=2)(wires=0)

    qml.Hadamard(wires=1)
    qml.ctrl(qml.S, control=2)(wires=1)

    qml.Hadamard(wires=2)

    qml.SWAP(wires=[0,2])

    return qml.state()

print("---\nchallenge 1")
print(three_qubit_QFT(0))

### challenge 2
dev = qml.device('default.qubit', wires=4)

def swap_bits(n_qubits):
    """A circuit that reverses the order of qubits, i.e.,
    performs a SWAP such that [q1, q2, ..., qn] -> [qn, ... q2, q1].
    
    Args:
        n_qubits (int): An integer value identifying the number of qubits.
    """

    for ind in range(0, n_qubits//2):
        qml.SWAP(wires=[ind, n_qubits-1-ind])
        

@qml.qnode(dev) 
def qft_node(basis_id, n_qubits):
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qml.BasisStatePreparation(bits, wires=range(n_qubits))
    # qft_rotations(n_qubits)
    swap_bits(n_qubits)
    return qml.state()

print("---\nchallenge 2")
print(qft_node(0, 3))

### challenge 3
dev = qml.device('default.qubit', wires=4)

def qft_rotations(n_qubits):
    """A circuit performs the QFT rotations on the specified qubits.
    
    Args:
        n_qubits (int): An integer value identifying the number of qubits.
    """

    for q in range(n_qubits):
        qml.Hadamard(wires=q)
        for rot in range(1, n_qubits-q):
            qml.ControlledPhaseShift(1/2**rot*np.pi, wires=[rot+q, q])


@qml.qnode(dev) 
def qft_node(basis_id, n_qubits):
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qml.BasisStatePreparation(bits, wires=range(n_qubits))
    qft_rotations(n_qubits)
    swap_bits(n_qubits)
    return qml.state()

print("---\nchallenge 3")
print(qft_node(0, 2))
drawer = qml.draw(qft_node)
print(drawer(0, 3))

### challenge 4
dev = qml.device('default.qubit', wires=4)

def qft_recursive_rotations(n_qubits, wire=0):
    """A circuit that performs the QFT rotations on the specified qubits
        recursively.
        
    Args:
        n_qubits (int): An integer value identifying the number of qubits.
        wire (int): An integer identifying the wire 
                    (or the qubit) to apply rotations on.
    """

    if wire == n_qubits:
        return

    qml.Hadamard(wires=wire)
    for i in range(wire+1, n_qubits):
        qml.ControlledPhaseShift(phi=1/2**(i-wire)*np.pi, wires=[i, wire])
    qft_recursive_rotations(n_qubits, wire=wire+1)


@qml.qnode(dev) 
def qft_node(basis_id, n_qubits):
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qml.BasisStatePreparation(bits, wires=range(n_qubits))
    qft_recursive_rotations(n_qubits)
    swap_bits(n_qubits)
    return qml.state()

print("---\nchallenge 4")
print(qft_node(0, 2))
drawer = qml.draw(qft_node)
print(drawer(0, 3))

### challenge 5
dev = qml.device('default.qubit', wires=4)

@qml.qnode(dev)
def pennylane_qft(basis_id, n_qubits):
    """A that circuit performs the QFT using PennyLane's QFT template.
    
    Args:
        basis_id (int): An integer value identifying 
            the basis state to construct.
        n_qubits (int): An integer identifying the 
            number of qubits.
            
    Returns:
        array[complex]: The state after applying the QFT to the qubits.
    """
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qml.BasisStatePreparation(bits, wires=range(n_qubits))

    qml.QFT(wires=range(n_qubits))

    return qml.state()

    
print("---\nchallenge 5")
print(pennylane_qft(0, 2))
drawer = qml.draw(pennylane_qft)
print(drawer(0, 3))
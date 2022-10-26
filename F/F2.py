import numpy as np
import pennylane as qml

### challenge 1
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def one_qubit_QFT(basis_id):
    """A circuit that computes the QFT on a single qubit. 
    
    Args:
        basis_id (int): An integer value identifying 
            the basis state to construct.
    
    Returns:
        array[complex]: The state of the qubit after applying QFT.
    """
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=dev.num_wires)]
    qml.BasisStatePreparation(bits, wires=[0])

    qml.Hadamard(wires=0)

    return qml.state()

print("---\nchallenge 1")
print(one_qubit_QFT(basis_id=0))


### challenge 2
n_bits = 2
dev = qml.device("default.qubit", wires=n_bits)

@qml.qnode(dev)
def two_qubit_QFT(basis_id):
    """A circuit that computes the QFT on two qubits using qml.QubitUnitary. 
    
    Args:
        basis_id (int): An integer value identifying the basis state to construct.
    
    Returns:
        array[complex]: The state of the qubits after the QFT operation.
    """
    
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=dev.num_wires)]
    qml.BasisStatePreparation(bits, wires=[0, 1])
    
    matrix = np.array([[1,1,1,1],[1,complex(0,1),-1, complex(0,-1)], [1,-1,1,-1],[1,complex(0,-1),-1,complex(0,1)]]) / n_bits
    qml.QubitUnitary(matrix, wires=[0,1])

    return qml.state()

print("---\nchallenge 2")
print(two_qubit_QFT(0))


### challenge 3
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def decompose_two_qubit_QFT(basis_id):
    """A circuit that computes the QFT on two qubits using elementary gates.
    
    Args:
        basis_id (int): An integer value identifying the basis state to construct.
    
    Returns:
        array[complex]: The state of the qubits after the QFT operation.
    """
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=dev.num_wires)]
    qml.BasisStatePreparation(bits, wires=[0, 1])

    qml.Hadamard(wires=0)
    qml.ctrl(qml.S, control=1)(wires=0)
    qml.Hadamard(wires=1)
    qml.SWAP(wires=[0,1])

    return qml.state()

print("---\nchallenge 3")
print(decompose_two_qubit_QFT(basis_id=0))

import numpy as np
import pennylane as qml

### challenge 1
dev = qml.device('default.qubit', wires=3)

@qml.qnode(dev)
def make_basis_state(basis_id):
    """Produce the 3-qubit basis state corresponding to |basis_id>.
    
    Note that the system starts in |000>.

    Args:
        basis_id (int): An integer value identifying the basis state to construct.
        
    Returns:
        array[complex]: The computational basis state |basis_id>.
    """

    binary = np.binary_repr(basis_id, 3)
    for ind, digit in enumerate(binary):
        if int(digit):
            qml.PauliX(wires=ind)
    
    return qml.state()


basis_id = 3
print("---\nchallenge 1")
print(f"Output state = {make_basis_state(basis_id)}")


### challenge 2
# Creates a device with *two* qubits
dev = qml.device('default.qubit', wires=2)

@qml.qnode(dev)
def two_qubit_circuit():
    qml.Hadamard(wires=0)
    qml.PauliX(wires=1)

    return qml.expval(qml.PauliY(wires=0)),qml.expval(qml.PauliZ(wires=1))

print("---\nchallenge 2")
print(two_qubit_circuit())

### challenge 3
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def create_one_minus():
    qml.PauliX(wires=0)
    qml.PauliX(wires=1)
    qml.Hadamard(wires=1)

    return qml.expval(qml.PauliZ(0)@qml.PauliX(1))

print("---\nchallenge 3")
print(create_one_minus())

### challenge 4
dev = qml.device('default.qubit', wires=2)

@qml.qnode(dev)
def circuit_1(theta):
    """Implement the circuit and measure Z I and I Z.
    
    Args:
        theta (float): a rotation angle.
        
    Returns:
        float, float: The expectation values of the observables Z I, and I Z
    """
    qml.RX(theta, wires=0)
    qml.RY(2*theta, wires=1)

    return qml.expval(qml.PauliZ(0)), qml.expval(qml.PauliZ(1))


@qml.qnode(dev)
def circuit_2(theta):
    """Implement the circuit and measure Z Z.
    
    Args:
        theta (float): a rotation angle.
        
    Returns:
        float: The expectation value of the observable Z Z
    """ 

    qml.RX(theta, wires=0)
    qml.RY(2*theta, wires=1)

    return qml.expval(qml.PauliZ(0)@qml.PauliZ(1))


def zi_iz_combination(ZI_results, IZ_results):
    """Implement a function that acts on the ZI and IZ results to
    produce the ZZ results. How do you think they should combine?

    Args:
        ZI_results (array[float]): Results from the expectation value of 
            ZI in circuit_1.
        IZ_results (array[float]): Results from the expectation value of 
            IZ in circuit_2.

    Returns:
        array[float]: A combination of ZI_results and IZ_results that 
        produces results equivalent to measuring ZZ.
    """

    combined_results = np.zeros(len(ZI_results))

    combined_results = np.multiply(ZI_results, IZ_results)

    return combined_results

 
theta = np.linspace(0, 2 * np.pi, 100)

# Run circuit 1, and process the results
circuit_1_results = np.array([circuit_1(t) for t in theta])

ZI_results = circuit_1_results[:, 0]
IZ_results = circuit_1_results[:, 1]
combined_results = zi_iz_combination(ZI_results, IZ_results)

# Run circuit 2
ZZ_results = np.array([circuit_2(t) for t in theta])

# Plot your results
#plot = plotter(theta, ZI_results, IZ_results, ZZ_results, combined_results)

print("---\nchallenge 4")



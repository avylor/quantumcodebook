import numpy as np
import pennylane as qml
from fractions import Fraction

### challenge 1
def U():
    qml.SWAP(wires=[2,3])
    qml.SWAP(wires=[1,2])
    qml.SWAP(wires=[0,1])
    for i in range(4):
        qml.PauliX(wires=i)

matrix = qml.matrix(U, wire_order=range(4))()

n_target_wires = 4
target_wires = range(n_target_wires)
n_estimation_wires = 3
estimation_wires = range(4, 4 + n_estimation_wires)


dev = qml.device("default.qubit", shots=1, wires=n_target_wires+n_estimation_wires)

@qml.qnode(dev)
def circuit(matrix):
    """Return a sample after taking a shot at the estimation wires.
    
    Args:
        matrix (array[complex]): matrix representation of U.

    Returns:
        array[float]: a sample after taking a shot at the estimation wires.
    """
    # CREATE THE INITIAL STATE |0001> ON TARGET WIRES
    qml.PauliX(wires=3)
    # USE THE SUBROUTINE QUANTUM PHASE ESTIMATION
    qml.QuantumPhaseEstimation(matrix, target_wires=target_wires, estimation_wires=estimation_wires)
    
    return qml.sample(wires=estimation_wires)

def get_phase(matrix):
    binary = "".join([str(b) for b in circuit(matrix)])
    return int(binary, 2) / 2 ** n_estimation_wires

print("---\nchallenge 1")

for i in range(5):
    print(circuit(matrix))
    print(f"shot {i+1}, phase:",get_phase(matrix))


### challenge 2
def U():
    qml.SWAP(wires=[2,3])
    qml.SWAP(wires=[1,2])
    qml.SWAP(wires=[0,1])
    for i in range(4):
        qml.PauliX(wires=i)

matrix = qml.matrix(U, wire_order=range(4))()

target_wires = range(4)
n_estimation_wires = 3
estimation_wires = range(4, 4 + n_estimation_wires)

def get_period(matrix):
    """Return the period of the state using the already-defined 
    get_phase function.
    
    Args:
        matrix (array[complex]): matrix associated with the operator U
        
    Returns:
        int: Obtained period of the state.
    """
    
    shots = 10
    period = 1
    for _ in range(shots):
        phase = get_phase(matrix)
        period = max(period, Fraction(phase).limit_denominator(2 ** n_estimation_wires).denominator)
    return period

print("---\nchallenge 2")
print(get_period(matrix))


### challenge 3
def U():
    qml.SWAP(wires=[2,3])
    qml.SWAP(wires=[1,2])
    qml.SWAP(wires=[0,1])
    for i in range(4):
        qml.PauliX(wires=i)

dev = qml.device("default.qubit", wires=4)

@qml.qnode(dev)
def circuit():
    """Apply U four times to |0001> to verify this is the period.
    
    Returns:
        array[float]: probabilities of each basis state. 
    """
    qml.PauliX(wires=3)
    for _ in range(4):
        U()
    return qml.probs(wires=range(4))


print("---\nchallenge 3")
print(circuit())



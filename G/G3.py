import numpy as np
import pennylane as qml

### challenge 1
n_bits = 5
query_register = list(range(n_bits))
aux = [n_bits]
all_wires = query_register+aux
dev = qml.device('default.qubit', wires=all_wires)

def oracle(combo):
    """Implement an oracle using a multi-controlled X gate.
    
    Args:
        combo (list): A list of bits representing the secret combination.
    """
    combo_str = ''.join(str(j) for j in combo)
    qml.MultiControlledX(wires=all_wires, control_values=combo_str)

print("---\nchallenge 1")
oracle([1,1,1,1,1])

### challenge 2
def hadamard_transform(my_wires):
    """Apply the Hadamard transform on a given set of wires.
    
    Args:
        my_wires (list[int]): A list of wires on which the Hadamard transform will act.
    """
    for wire in my_wires:
        qml.Hadamard(wires=wire)

def diffusion():
    """Implement the diffusion operator using the Hadamard transform and 
    multi-controlled X."""

    hadamard_transform(query_register)
    qml.MultiControlledX(wires=range(n_bits+1), control_values=n_bits*'0')
    hadamard_transform(query_register)

print("---\nchallenge 2")
diffusion()

### challenge 3
@qml.qnode(dev)
def grover_circuit(combo):
    """Apply the MultiControlledX Grover operator and return probabilities on 
    query register.
    
    Args:
        combo (list[int]): A list of bits representing the secret combination.

    Returns:
        array[float]: Measurement outcome probabilities.
    """
    
    hadamard_transform(query_register)
    qml.PauliX(wires=aux)
    qml.Hadamard(wires=aux)
    oracle(combo)
    diffusion()
    return qml.probs(wires=query_register)

print("---\nchallenge 3")
print(grover_circuit([0,0,0,0,0]))

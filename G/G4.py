import numpy as np
import pennylane as qml

### challenge 1

def oracle(combo):
    """Implement an oracle using a multi-controlled X gate.
    
    Args:
        combo (list): A list of bits representing the secret combination.
    """
    combo_str = ''.join(str(j) for j in combo)
    qml.MultiControlledX(wires=range(len(combo)+1), control_values=combo_str)

def hadamard_transform(my_wires):
    """Apply the Hadamard transform on a given set of wires.
    
    Args:
        my_wires (list[int]): A list of wires on which the Hadamard transform will act.
    """
    for wire in my_wires:
        qml.Hadamard(wires=wire)

def diffusion(n_bits):
    """Implement the diffusion operator using the Hadamard transform and 
    multi-controlled X."""

    hadamard_transform(range(n_bits))
    qml.MultiControlledX(wires=range(n_bits+1), control_values=n_bits*'0')
    hadamard_transform(range(n_bits))


def grover_iter(combo, num_steps):
    """Run Grover search for a given secret combination and a number of iterations.
    
    Args:
        combo (list[int]): The secret combination, represented as a list of bits.
        num_steps (int): The number of Grover iterations to perform.

    Returns: 
        array[float]: Probability for observing different outcomes.
    """
    n_bits = len(combo)
    query_register = list(range(n_bits))
    aux = [n_bits]
    all_wires = query_register+aux
    dev = qml.device('default.qubit', wires=all_wires)

    @qml.qnode(dev)
    def inner_circuit():
        hadamard_transform(query_register)
        qml.PauliX(wires=aux)
        qml.Hadamard(wires=aux)
        for _ in range(num_steps):
            oracle(combo)
            diffusion(n_bits)
        return qml.probs(wires=query_register)
    
    return inner_circuit()

print("---\nchallenge 1")
print(grover_iter([0,0,0,0], 5))

### challenge 2
n_list = range(3,7)
opt_steps = []

for n_bits in n_list:
    combo = "0"*n_bits # A simple combination
    step_list = range(1,10) # Try out some large number of steps
    probs = []
    for num_steps in step_list:
        prob = grover_iter(combo, num_steps)[0]
        probs.append(prob)
    #opt_steps.append(local_max_arg(probs)) # TODO uncomment for submission


print("---\nchallenge 2")
print("The optimal number of Grover steps for qubits in", [3,4,5,6], "is", opt_steps, ".")


### challenge 3
grad = 0.5
intercept = -0.47
# SUBMIT TO PLOT GRAPH
print("---\nchallenge 3")




import numpy as np
import pennylane as qml

### challenge 1
n_bits = 5
query_register = list(range(n_bits))
aux = [n_bits]
all_wires = query_register+aux
dev = qml.device('default.qubit', wires=all_wires)

def oracle_multi(combos):
    """Implement multi-solution oracle using sequence of multi-controlled X gates.
    
    Args:
        combos (list[list[int]]): A list of solutions.
    """
    for combo in combos:
        combo_str = ''.join(str(j) for j in combo)
        qml.MultiControlledX(wires=range(len(combo)+1), control_values=combo_str)

print("---\nchallenge 1")
oracle_multi([[0,0,0,0,0]])


### challenge 2
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


n_bits = 5
query_register = list(range(n_bits))
aux = [n_bits]
all_wires = query_register+aux
dev = qml.device('default.qubit', wires=all_wires, shots=None)

def grover_iter_multi(combos, num_steps):
    """Run Grover search for multiple secret combinations and a number 
    of Grover steps.
    
    Args:
        combos (list[list[int]]): The secret combination, represented as a list of bits.
        num_steps (int): The number of Grover iterations to perform.

    Returns: 
        array[float]: Probability for observing different outcomes.
    """
    @qml.qnode(dev)
    def inner_circuit():
        qml.PauliX(wires=n_bits)
        qml.Hadamard(wires=n_bits)
        hadamard_transform(query_register)

        for _ in range(num_steps):
            oracle_multi(combos)
            diffusion(n_bits)
        return qml.probs(wires=query_register)
    
    return inner_circuit()

print("---\nchallenge 2")
print(grover_iter_multi([[0,0,0,0,0],[0,0,0,0,1]], 5))

### challenge 3
m_list = range(3)
opt_steps = []

for m_bits in m_list:
    combos = [[int(s) for s in np.binary_repr(j, n_bits)] for j in range(2**m_bits)]
    step_list = range(1,10)
    probs = []
    for num_steps in step_list:
        prob = np.sum(grover_iter_multi(combos, num_steps)[:len(combos)])
        probs.append(prob)
    #opt_steps.append(local_max_arg(probs)) # TODO uncomment for submission

print("---\nchallenge 3")
print("The optimal number of Grover steps for the number of solutions in", [1,2,4], "is", opt_steps, ".")


### challenge 4
grad = -0.5
intercept = 2.03
# SUBMIT TO PLOT GRAPH
print("---\nchallenge 4")


### challenge 5
print("---\nchallenge 5")
print("empty challenge")


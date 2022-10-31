import numpy as np
import pennylane as qml

### challenge 1
def is_equivalent(a, b, m):
    """Return a boolean indicating whether the equivalence is satisfied.

    Args:
        a (int): First number to check the equivalence.
        b (int): Second number to check the equivalence.
        m (int): Modulus of the equivalence.
    
    Returns:
        bool: True if a = b (m), False otherwise.
    """
    if (a-b) % m == 0:
        return True
    return False

print("---\nchallenge 1")
print(f"13 = 8 (3) is {is_equivalent(13, 8, 3)}")
print(f"13 = 7 (6) is {is_equivalent(13, 7, 6)}")


### challenge 2
def has_inverse(a, m):
    """Returns a boolean indicating whether a number has an inverse modulo m.
    
    Args:
        a (int): Number to find the inverse modulus m.
        m (int): Modulus of the equivalence.

    Returns:
        bool: True if c exists (ac = 1 (m)), False otherwise    
    """
    
    if np.gcd(a,m) > 1:
        return False
    return True
    
print("---\nchallenge 2")
print("(5,15)", has_inverse(5,15))
print("(7,15)", has_inverse(7,15))

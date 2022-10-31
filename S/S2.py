import numpy as np
import pennylane as qml

### challenge 1
def nontrivial_square_root(m):
    """Return the first nontrivial square root modulo m.
    
    Args:
        m (int): modulus for which want to find the nontrivial square root

    Returns:
        int: the first nontrivial square root of m
    """
    
    for i in range(2, m):
        if (i*i - 1) % m == 0:
            return i
        
print("---\nchallenge 1")
print(nontrivial_square_root(391))


### challenge 2
def factorization(N):
    
    """Return the factors of N.
    
    Args:
        N (int): number we want to factor.

    Returns:
        array[int]: [p,q] factors of N.
    """
    x = nontrivial_square_root(N)
    return np.gcd(x-1, N), np.gcd(x+1, N)

N = 391
p, q = factorization(N)

print("---\nchallenge 2")
print(f"{N} = {p} x {q}")

### challenge 3
print("---\nchallenge 3")
print("empty challenge")




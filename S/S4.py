import numpy as np
import pennylane as qml

### challenge 1
def is_coprime(a, N):  
    """Determine if two numbers are coprime.
        
    Args:
        a (int): First number to check if is coprime with the other.
        N (int): Second number to check if is coprime with the other.
        
    Returns:
        bool: True if they are coprime numbers, False otherwise.
    """
    
    if np.gcd(a, N) > 1:
        return False
    return True
    

def is_odd(r):
    """Determine if a number is odd.   
    
    Args:
        r (int): Integer to check if is an odd number.
        
    Returns:
        bool: True if it is odd, False otherwise.
    """
    
    if r % 2 == 1:
        return True
    return False


def is_not_one(x, N):
    """Determine if x is not +- 1 modulo N.
    
    Args:
        N (int): Modulus of the equivalence.
        x (int): Integer to check if it is different from +-1 modulo N.
        
    Returns:
        bool: True if it is different, False otherwise.
    """
    
    result = x % N
    if x == 1 or x == N-1:
        return False
    return True
    
print("---\nchallenge 1")
print("3 and 12 are coprime numbers: ", is_coprime(3,12))
print("5 is odd: ", is_odd(5))
print("4 is not one mod 5: ",is_not_one(4,5))


### challenge 2

def shor(N):
    """Return the factorization of a given integer.
   
    Args:
       N (int): integer we want to factorize.
    
    Returns:
        array[int]: [p,q], the prime factors of N.
    """
        
    while(True):
        a = np.random.randint(2, N-1)
    
        if not is_coprime(a, N):
            p = np.gcd(a, N)
            return p, N/p
        
        period = 6
        # U = get_matrix_a_mod_N(a, N) # TODO uncomment for submission
        # period = get_period(U, N) # TODO uncomment for submission

        if not is_odd(period):
            x = np.power(a, int(period/2)) % N
            
            if is_not_one(x,N):
                return np.gcd(x-1, N), np.gcd(x+1, N)
        
print("---\nchallenge 2")
print(shor(21))

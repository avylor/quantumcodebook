import numpy as np
import pennylane as qml

### challenge 1
def create_keys(p, q):
    """Returns the characteristic e, d and N values of RSA
    
    Args:
        p (int): First prime number of the algorithm.
        q (int): Second prime number of the algorithm.
        
    Returns:
        (int, int, int): a tuple consisting of the 'e' value of the RSA codification. 'd' value of the RSA codification.
            and 'N', the product of p and q.
    """
    
    theta = (p-1)*(q-1)
    e = p
    d = pow(e,-1, theta)
    return e,d,p*q

print("---\nchallenge 1")
print(create_keys(3,53))


### challenge 2
def decode(d,N, code):
    """Decode an encrypted message
    
    Args:
        d (int): Value of the RSA codification.
        N (int): Product of p and q.
        code list[int]: List of values to be decoded.
        
    Returns:
        string: Decoded message. (One character per list item)
    """
    
    message = ''.join([chr((c**d)%N) for c in code])
    return message

code =  [129827,
         294117,
         126201,
         157316,
         270984,
         126201,
         157316,
         270984,
         209269,
         163084,
         270984,
         157316,
         95353,
         289896,
         49377,
         95353,
         48004,
         270984,
         209269,
         95353,
         157316,
         157316,
         210673,
         267093,
         95353]

N = 378221
d = 150797

print("---\nchallenge 2")
print(decode(d, N, code))

### challenge 3

print("---\nchallenge 3")


### challenge 4

print("---\nchallenge 4")



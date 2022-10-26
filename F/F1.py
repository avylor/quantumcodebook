import numpy as np
import pennylane as qml

### challenge 1
def coefficients_to_values(coefficients):
    """Returns the value representation of a polynomial
    
    Args:
        coefficients (array[complex]): a 1-D array of complex 
            coefficients of a polynomial with 
            index i representing the i-th degree coefficient

    Returns: 
        array[complex]: the value representation of the 
            polynomial 
    """
    return np.fft.fft(coefficients)

A = [4, 3, 2, 1]

print("---\nchallenge 1")
print(coefficients_to_values(A))


### challenge 2
def values_to_coefficients(values):
    """Returns the coefficient representation of a polynomial
    
    Args:
        values (array[complex]): a 1-D complex array with 
            the value representation of a polynomial 

    Returns: 
        array[complex]: a 1-D complex array of coefficients
    """
    
    return np.fft.ifft(values)

A = [10.+0.j,  2.-2.j,  2.+0.j,  2.+2.j]

print("---\nchallenge 2")
print(values_to_coefficients(A))


### challenge 3
def nearest_power_of_2(x):
    """Given an integer, return the nearest power of 2. 
    
    Args:
        x (int): a positive integer

    Returns: 
        int: the nearest power of 2 of x
    """
    return int(2**(np.ceil(np.log2(x))))

print("---\nchallenge 3")
print(nearest_power_of_2(17))


### challenge 4
def fft_multiplication(poly_a, poly_b):
    """Returns the result of multiplying two polynomials
    
    Args:
        poly_a (array[complex]): 1-D array of coefficients 
        poly_b (array[complex]): 1-D array of coefficients 

    Returns: 
        array[complex]: complex coefficients of the product
            of the polynomials
    """

    # Calculate the number of values required
    # Figure out the nearest power of 2
    nr = nearest_power_of_2(len(poly_a) + len(poly_b) - 1)
    print(nr)
    # Pad zeros to the polynomial
    poly_a = np.pad(poly_a, (0,nr-len(poly_a)), 'constant', constant_values=0)
    poly_b = np.pad(poly_b, (0,nr-len(poly_b)), 'constant', constant_values=0)
    # Convert the polynomials to value representation
    fft_a = np.fft.fft(poly_a) 
    fft_b = np.fft.fft(poly_b) 
    # Multiply
    result = np.multiply(fft_a, fft_b)
    # Convert back to coefficient representation
    return np.fft.ifft(result)

print("---\nchallenge 4")
print(fft_multiplication([1,1], [1,1]))

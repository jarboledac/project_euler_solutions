"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import numpy as np

def list_multiplications(n_digits: int) -> list:
    """
    The function return the posibles values resulting of n_digits size 
    multiplication

    Parameters
    ----------
        n_digits: int
            number digits in the number multiplication
    Return
    ------
        Return list of multiplications of n_digits size
    """
    numbers_quantity = 10**n_digits
    possible_numbers = np.array(range(1,numbers_quantity+1)) \
                                .reshape((numbers_quantity,-1))
    possible_combis = np.matmul(possible_numbers, possible_numbers.T)
    result_combis = possible_combis[np.tril_indices(numbers_quantity)]
    return result_combis

palindromes = lambda x: str(x) == str(x)[::-1]

if __name__ == '__main__':
    size_digits = int(input("Input the size of digits in multiplication : "))
    possible_multi = list_multiplications(size_digits)
    max_palindrome = max(list(filter(palindromes, possible_multi)))
    print(f'\nThe greatest palindrome made from the product of two {size_digits}-digit numbers is {max_palindrome}')
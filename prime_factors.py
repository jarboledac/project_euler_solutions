"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""
from typing import Callable

def lowest_factor(number: int):
    """
    The function return the lowest factor prime for a number

    Parameters
    ----------
        number: int
            number to calculate lowest factor
    Return
    ------
        Return lowest factor prime and quotient 
    """
    for divisor in range(2,number+1):
        if number % divisor == 0:
            number = int(number/divisor)
            return number, divisor

def prime_factors(number: int, fun_lowest_factor: Callable[[int], int] = lowest_factor) -> list:
    """
    The function return the prime factors for a number

    Parameters
    ----------
        number: int
            number to calculate the prime factors
        fun_lowest_factor: function
            function to return the lowest factor prime for a number
    Return
    ------
        Return list of prime factors for a number 
    """
    primes_factors = []
    while number != 1:
        number, min_factor = fun_lowest_factor(number)
        primes_factors.append(min_factor)
    return primes_factors

#n = 600851475143

if __name__ == '__main__':
    num_factors = int(input("Input a number to calculate the greatest prime factor : "))
    primes_factors = prime_factors(num_factors)
    print(f'The greates prime factor to the number {num_factors} is {primes_factors[-1]}')
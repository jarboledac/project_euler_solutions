"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible, divisible with no remainder, by all of the numbers from 1 to 20?
"""
import numpy as np

##232792560 solutio

def smallest_divisible(cant_evaluate: int) -> int:
    num_validate = cant_evaluate
    while True:
        modulo_array = num_validate%np.arange(1,cant_evaluate +1)
        if modulo_array.sum() != 0:
            num_validate += cant_evaluate
        else: 
            print(f'Cumple y el número es {num_validate}')
            return num_validate

if __name__ == '__main__':
    cant_evaluate = int(input("Input a upper limit in the range : "))
    smallest_divisible(cant_evaluate)
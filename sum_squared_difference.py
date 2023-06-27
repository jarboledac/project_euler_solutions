"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385.
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025.
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def dif_sum_squared(n_lim: int) -> int:
    """
    Calculates the difference between the square of the sum of natural numbers and the 
    sum of squares of them

    Input:
        n_lim : int
            The upper limit of the natural numbers.

    Returns:
        int: The difference between the sum of squares and the square of the sum.

    """
    natural_numbers = range(1,n_lim+1)
    return sum(natural_numbers)**2-sum([x**2 for x in natural_numbers])


if __name__ == '__main__':
    sup_limit = int(input("Input a upper limit in the range : "))
    print(dif_sum_squared(sup_limit))
"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def fibonnacci_even(n: int) -> int:
    """
    Obtaing the n even element from fibonacci sequence

    Input
    -----
        n: int
            n even element
    Return
    ------
        Value for the n even element in fibonacci sequence
    """
    if n == 0 or n<0:
        return 0
    elif n == 1:
        return 2
    return 4*fibonnacci_even(n-1) + fibonnacci_even(n-2)




if __name__ == '__main__':
    limit_value = int(input('Input limit value in fibonacci sequence :'))
    sum_fibonacci = 0
    n = 0
    while True:
        value_n = fibonnacci_even(n)
        if value_n > limit_value:
            break
        else:
            sum_fibonacci += value_n
            n += 1
    print(sum_fibonacci)
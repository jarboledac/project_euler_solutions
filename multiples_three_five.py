"""
Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 
5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum 
of all the multiples of 3 or 5 below 1000.
"""

multiple_three_five = lambda x : (x%3==0) or (x%5==0)


if __name__ == '__main__':
    n_lim = int(input(f' Input the superior limit : '))
    sum_values = sum(list(filter(multiple_three_five, range(1, n_lim))))
    print(f'The result of sum is : {sum_values}')
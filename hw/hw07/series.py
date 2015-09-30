
# Part One 
# test_fibonacci_series

import math

def fibonacci(n):

    n=int(n)
    
    if n:
        if n == 0:
            return 0
        elif n == 1:
            return 1
    else:
        return ('fibonacci',((n-1)+f(n+1)))

# Part Two 
# test_lucasnumbers

def lucas(n):

    n=int(n)

    if n:
        if n == 2:
            return 2
        elif n == 1:
            return 1
    else:
        return ('lucas',((n-1)+l(n+1)))

# Part Three
# sum_series

def sum(n):

    n=int(n)

    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print("It's Fibonacci series!",((n-1)+f(n+1)))

    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        print("It's Lucas numers!",((n-1)+l(n+1)))

                    
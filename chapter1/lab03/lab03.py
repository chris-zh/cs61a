# coding:utf-8
# Q2
def make_buzzer(n):
    """ Returns a function that prints numbers in a specified
    range except those divisible by n.

    >>> i_hate_fives = make_buzzer(5)
    >>> i_hate_fives(10)
    Buzz!
    1
    2
    3
    4
    Buzz!
    6
    7
    8
    9
    """
    "*** YOUR CODE HERE ***"
    def buzzer(range):
        i = 0
        while i < range:
            if i % n == 0:
                print('Buzz!')
            else:
                print(i)
            i += 1
    return buzzer


# Q4
def f1():
    """
    >>> f1()
    3
    """
    "*** YOUR CODE HERE ***"
    return 3

def f2():
    """
    >>> f2()()
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda: 3

def f3():
    """
    >>> f3()(3)
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda x:  x

def f4():
    """
    >>> f4()()(3)()
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda : lambda x: lambda: x

# Q6
def sum(n):
    """Computes the sum of all integers between 1 and n, inclusive.
    Assume n is positive.

    >>> sum(1)
    1
    >>> sum(5)  # 1 + 2 + 3 + 4 + 5
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return n
    return n + sum(n - 1)

# Q7
##边界条件缺失
def sum_every_other_number(n):
    """Return the sum of every other natural number 
    up to n, inclusive.

    >>> sum_every_other_number(8)
    20
    >>> sum_every_other_number(9)
    25
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum_every_other_number(n - 2)

##没有正确return结果
def fibonacci(n):
    """Return the nth fibonacci number.
    
    >>> fibonacci(11)
    89
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Q8
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return n
    else:
        print(n)
        if n % 2 ==0:
            return hailstone(n // 2)
        else:
            return hailstone(n * 3 + 1)
#Q9
def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher order function
    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def g(n):
        if n % 3 == 0:
            return f3
        elif n % 3 == 1:
            return f1
        elif n % 3 == 2:
            return f2
    def h(n):
        if n == 0:
            return lambda x: x
        else:
            return lambda x: g(n)(h(n - 1)(x))
    return h
#Q10
def lambda_curry2(func):
    return lambda x: lambda y: func(x, y)
#Q11
20
#Q12
def path(m, n):
    return 0
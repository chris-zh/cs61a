__author__ = 'Administrator'
from operator import add, sub
def a_plus_abs_b(a, b):
    if b < 0:
        f = sub
    else:
        f = add
    return f(a,b)
print(a_plus_abs_b(1,-2))
print(a_plus_abs_b(1,2))
print(a_plus_abs_b(1,0))



__author__ = 'Administrator'
from operator import add, sub
#Question 1
def a_plus_abs_b(a, b):
    if b < 0:
        f = sub
    else:
        f = add
    return f(a,b)
print(a_plus_abs_b(1,-2))
print(a_plus_abs_b(1,2))
print(a_plus_abs_b(1,0))

#Question 2
def two_of_three(a, b, c):
	return pow(a,2)+pow(b,2)+pow(c,2)-pow(min(a,b,c),2)
print(two_of_three(1,2,3))

#Question 3
##the given function
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result
##the required function
def with_if_statement():
	if c():
		return t()
	else:
		return f()
def with_if_function():
	return if_function(c(), t(), f())
def t():
	return 1
def c():
	return True
def f():
	return 2/0
"""
执行结果：
>>> with_if_function()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    with_if_function()
  File "<pyshell#64>", line 2, in with_if_function
    return if_function(c(), t(), f())
  File "<pyshell#74>", line 2, in f
    return 2/0
ZeroDivisionError: division by zero
>>> with_if_statement()
1
"""
###解释：这是一个关于正则序和应用序的例子。
###当调用with_if_statement()时，先对c()求值，结果为True，则执行if语句，对t()求值。可得出正确结果1。
###此时并不会对f()求值
###当调用with_if_function()时，在return语句中又调用了if_function()，此时会对c(),t(),f()三个函数求值。
###因此在对f()求值时，报错。



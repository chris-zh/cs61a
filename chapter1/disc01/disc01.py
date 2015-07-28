#1.3 Questions 
def is_prime(n):
    assert type(n) ==int, 'n must be an integer'
    assert n >= 0, 'n must be a positive number'
    if n == 1 or n == 0 :
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True
#1.4 Extra Questions
def choose(n, k):
    """Returns the number of ways to choose K items from N items.
    >>> choose(5, 2)
    10
    >>> choose(20, 6)
    38760
    """
    i, numer = 0, 1
    while i < k:
        numer = numer * (n - i)
        i += 1
    j, denom = 0, 1
    while j < k:
        denom = denom * (k - j)
        j += 1
    return numer // denom
##optimized
def choose2(n, k):
    i, numer, denom = 0, 1, 1
    while i < k:
        numer = numer * (n - i)
        denom = denom * (k - i)
        i += 1
    return numer // denom
##optimized another
def choose3(n, k):
    i, result = 0, 1
    while i < k:
        result = result * (n - i)/(k-i)#这里有精度问题
        i += 1
    return result
#2.1 Functions as Argument Values
#2.2 Questions
def square(x):
    return x * x
def square_ints(n):
    i = 1
    while i <= n:
        print(square(i))
        i += 1
def double(x):
    return 2 * x
def double_ints(n):
    i = 1
    while i <= n:
        print(double(i))
        i += 1
def cube(x):
    return x * x * x
def transform_ints(func, n):
    i = 1
    while i <= n:
        print(func(i))
        i += 1
def square_ints_opt(n):
    transform_ints(square, n)
def double_ints_opt(n):
    transform_ints(double, n)
def cube_ints_opt(n):
    transform_ints(cube, n)
#2.3 Functions as Return Values
#2.4 Questions
## 1
def and_add(f, n):
    def add_n(x):
        return f(x) + n
    return add_n
## 2
'''a diagram, pass。结果是15'''
#2.5 Extra Questions
## 1
def keep_ints(cond, n):
    i = 1
    while i < n:
        if cond(i):
            print(i)
        i += 1
## 2
'''
4
11
2
'''
## 3
'''a diagram, pass。结果是5'''
#3.1 Questions
## 1
a = 1
def b(b):
    return a + b
a = b(a)
a = b(a)
'''这道题目知识点是关于变量的取值，根据John教授所说，变量的取值为：第一次出现的frame中取值，
然后再去看parent frame.a = b(a)第一次调用时，a为global frame中的1，在b函数内部，a同样为
global frame中的1,而b为传进来的a，也就是1，因此返回结果为2，赋值给a，因此global frame中
的a变为2.第二次调用，a为2传给b，b中的a为global frame中的2，b为传进来的a，因此返回为4，再给
a赋值，global frame中的a变为4'''
## 2
'''同上一题同样的道理。this(that(y))返回结果应该为6。这里的坑是that 函数中定义的x，
为that frame中的变量，最后直接返回x，与传入的x无关。同样that函数中的this也是局部变量，
作用域仅限于that frame,与global frame中的this函数无关。'''
#3.2 Extra Questions
'''同上一个问题.six = 6, spring = 36'''


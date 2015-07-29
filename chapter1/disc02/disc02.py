# coding:utf-8
# n*(n-1)*(n-2)...*2*1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n -1)
#--------------------------------------------
#1.1 Cool Questions!
##1
def countdown(n):
    if n == 1:
        print(n)
    else:
        print(n)
        countdown(n - 1)
#--------------------------------------------
##2
'''将print放在最后，每次调用都累计了一个print尚未执行。当递归完成之后，去执行
所有的print'''
def countup(n):
    if n == 1:
        print(n)
    else:
        countup(n - 1)
        print(n)
#--------------------------------------------
##3
'''递归问题的 步骤：1、先找到最基本的条件。2、假设递归函数存在，用最简单的条件去调用
3、用递归函数去解决整个问题域'''
def expt(base, power):
    assert power >=0, 'power must be an positive integer!'
    if power == 1:
        return base
    elif power ==0:
        return 1
    else:
        return expt(base, power - 1) * base
#--------------------------------------------
##4
'''这算是作弊吧233'''
def is_prime(n):
    def prime(num, div=2):
        assert num > 0, 'n must be a positive integer'
        if num == div :
            return True
        elif num % div ==0 or num == 1:
            return False
        else:
            return prime(num, div + 1)
    return prime(n)
#--------------------------------------------
##5
def sum_primes_up_to(n):
    return sum(list(filter(is_prime, range(n + 1)[2:])))


def test():
    '''print(is_prime(2))
    print(is_prime(1))
    print (is_prime(98))
    print (is_prime(7))
    print (is_prime(1937))'''
    print(sum_primes_up_to(20))
if __name__=='__main__':
    test()
#--------------------------------------------
##6
'''rec(3, 2) 3的2次方'''
def rec(x, y):
    if y > 0:
        return x * rec(x, y - 1)
    return 1
#--------------------------------------------
#2.1 Exercises
##1
'''看起来跟SICP第一章换硬币的问题很类似。'''
'''下面的写法是错的，待解决'''
def count_stair_ways(n):
    def cc(amount, kinds_of_cons):
        if amount ==0:
            return 1
        elif amount < 0 or kinds_of_cons ==0:
            return 0
        else:
            return cc(amount, kinds_of_cons - 1) + cc(amount - 2, kinds_of_cons)
    return cc(n, 2)


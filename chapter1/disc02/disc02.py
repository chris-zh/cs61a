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
'''斐波那契数列'''
'''问题扩展：SICP第一章换硬币的问题'''
def count_stair_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n-1)+count_stair_ways(n-2)

###2
'''帕斯卡三角'''
def pascal(row, column):
    if row == 0:
        return 1
    elif column ==0 or row == column:
        return 1
    else:
        return pascal(row - 1, column -1) +pascal(row - 1, column)
###3
'''类似找零钱的问题'''
def has_sum(sum, n1, n2):
    def cc(amount, kinds_of_coins):
        if amount == 0:
            return 1
        elif amount < 0 or kinds_of_coins == 0:
            return 0
        else:
            return cc(amount, kinds_of_coins - 1) + cc(amount - first_denomination(kinds_of_coins), kinds_of_coins)
    def first_denomination(kinds_of_coins):
        if kinds_of_coins == 1:
            return n1
        elif kinds_of_coins == 2:
            return n2
    #return cc(sum, 2)
    if cc(sum, 2) > 0:
        return True
    return False

'''下面是找零钱问题
def count_change(amount):
    return cc(amount, 2)

def cc(amount, kinds_of_coins):
    if amount == 0:
        return 1
    elif amount < 0 or kinds_of_coins == 0:
        return 0
    else:
        return cc(amount, kinds_of_coins - 1) + cc(amount - first_denomination(kinds_of_coins), kinds_of_coins)

def first_denomination(kinds_of_coins):
    if kinds_of_coins == 1:
        return 1
    elif kinds_of_coins == 2:
        return 5
    elif kinds_of_coins ==3:
        return 10
    elif kinds_of_coins == 4:
        return 25
    elif kinds_of_coins ==5:
        return 50
    else:
        return 0
'''

##2.2 Extra Questions
def sum_range(lower, upper):
    def predicate(low, up):
        if low < 50 and up >= 60:
            return True
        elif 50 < low <= 130 and up >= 140:
            return True
        elif 130 < low <= 180 and up >= 200:
            return True
        else:
            return False
    if lower > 200:
        return sum_range(lower - 200, upper - 200)
    else:
        return predicate(lower, upper)

def test():
    print(sum_range(45, 60))
    print(sum_range(40, 55))
    print (sum_range(170, 201))
    print(sum_range(249, 260))
if __name__=='__main__':
    test()
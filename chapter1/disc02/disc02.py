# n*(n-1)*(n-2)...*2*1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n -1)
#1.1 Cool Questions!
##1
def countdown(n):
    if n == 1:
        print(n)
    else:
        print(n)
        countdown(n - 1)
##2
'''这里比较屌啊，将print放在最后，每次调用都累计了一个print尚未执行。当递归完成之后，去执行
所有的print'''
def countup(n):
    if n == 1:
        print(n)
    else:
        countup(n - 1)
        print(n)
##3
'''递归问题的 步骤：1、先找到最基本的条件。2、假设递归函数存在，用最简单的条件去调用
3、用递归函数去解决整个问题域'''
def expt(base, power):
    if power == 1:
        return base
    else:
        return expt(base, power - 1) * base

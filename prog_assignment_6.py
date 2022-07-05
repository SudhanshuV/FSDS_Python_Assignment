import math
def fibonacci(n):
    ''''print n elements fron fibboniciseries'''
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
for i in range(8):
    print(fibonacci(i))


def factorial(n):
    '''print factorail of given number'''
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(6))


def bmi_cal(h,w):
    '''calculate bmi for given hieght (m) and weight (kg)'''
    return (w/h**2)

print(bmi_cal(1.6,51))

def log_10():
    '''calcualte log for given value and base'''
    i=int(input('enter value: '))
    j=int(input('enter base : '))
    return math.log(i,j)

print(log_10())

def sum_cube(n):
    '''returns sum of cube of given number of element'''
    sm=0
    for i in range(1,n+1):
        sm=sm+(i**3)
    return sm

print(sum_cube(10))
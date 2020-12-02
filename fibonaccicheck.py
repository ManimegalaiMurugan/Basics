import math
num = int(input("Enter the number to check whelter it is a fibonacci number or not"))

def perfectsqrt(n):
    sqrrt = int(math.sqrt(n))
    return (sqrrt * sqrrt == n)

def fibonacci(num):
    return perfectsqrt(5*num*num+4) or perfectsqrt(5*num*num-4)



if fibonacci(num):
    print("{} is a fibonnaci number".format(num))
else :
    print("{} is not a fibonnaci number".format(num))

''' inpu = int(input("Enter the number to do factorial"))
def factorial(num):
    fact = 1
    while num > 0 :
        fact = fact * num
        num=num-1
    return fact      
print(factorial(inpu)) '''


#recursion factorial
inpu = int(input("Enter the number to do factorial"))
def factorial(num):
   
    
        if(num == 1):
            return 1
        else:
            return ((num) * (factorial(num-1)))
    
print(factorial(inpu))

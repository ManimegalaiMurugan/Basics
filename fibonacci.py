num = int(input("Enter the number to get fibonnaci series"))
n1 = 0
n2 = 1
lists = []
def fibonaccii(num,n1,n2):
        if num > 0 :
            n3 = n1 + n2
            n1 =n2
            n2 = n3
            lists.append(n3)
            fibonaccii(num-1,n1,n2)  
   

lists.append(n1)
lists.append(n2)
fibonaccii(num-2,n1,n2)


for i in lists :
        print(i)


===============================================
num = int(input("Enter the number to get fibonnaci series"))
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
  
# Driver Program 
  
print(Fibonacci(num))

===========================================
num = int(input("Enter the number to get fibonnaci series"))
n1 = 0
n2 = 1
lists = []
def fibonaccii(num,n1,n2):
        if num > 0 :
            n3 = n1 + n2
            n1 =n2
            n2 = n3
            lists.append(n3)
            fibonaccii(num-1,n1,n2)  
   

lists.append(n1)
lists.append(n2)
fibonaccii(num-2,n1,n2)

for i in lists :
        print(i)


if num in lists :
         print('yes')
else :
        print('no')
  

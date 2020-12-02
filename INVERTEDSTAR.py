num = int(input("Enter a number to print inverted star : "))
for i in range(0,num):
    print(" " * i , "*" * (num - i))

Enter a number to print inverted star : 5
 *****
  ****
   ***
    **
     *
=======================================================


num = int(input("Enter a number to print inverted star : "))
for i in range(1,num+1):
    print("*" * i , " " * (num - i))

Enter a number to print inverted star : 5
*     
**    
***   
****  
*****

=========================================================

num = int(input("Enter a number to print inverted star : "))

for i in range(0,num):
    print( "*" * (num - i)," " * i )

Enter a number to print inverted star : 5
***** 
****  
***   
**    
*

=========================================================

num = int(input("Enter a number to print inverted star : "))

for i in range(0,num):
    print(" " * i , "*" * (num - i))

Enter a number to print inverted star : 5
 *****
  ****
   ***
    **
     *

=====================================================




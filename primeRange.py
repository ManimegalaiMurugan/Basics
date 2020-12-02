startRange = int(input("Enter the starting range of input"))
endRange = int(input("Enter the ending range of input"))
lists = []
for i in range(startRange,endRange+1) :
    count = 0;
    if i != 1:
        for j in range(2,i) :
            if i % j == 0 :
                count = 1
                break;
        if count == 0 :
            lists.append(i)
for s in lists:
    print(s)

Enter the starting range of input1
Enter the ending range of input20
2
3
5
7
11
13
17
19

=======================================================

num =int(input("enter the numberto check whether it is prime or not : "))
lists = []
count = 0
for i in range(2,num):
    if num % i == 0:
        count = 1
        break;
if count == 0 :
    print(" {} is a prime number ".format(num))
else :
    print("{} is not a prime number ".format(num))

enter the numberto check whether it is prime or not : 3
 3 is a prime number
 
=======================================================
        

            
        

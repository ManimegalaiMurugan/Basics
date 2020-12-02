num=int(input("Enter the number to whelter it is armstrong number or not"))
temp=num
count = 0
output=0
lists=[]
while temp > 0 :
    count =count + 1
    lists.append(temp%10)
    temp=int(temp/10)

for i in lists:
   output = int(output + pow(i,count))
   #print(output)
if(num == output):
    print('{} is a armstrong number'.format(num))
else:
    print('{} is not a armstrong number'.format(num)) 


========================================================
num=input("Enter the number to whelter it is armstrong number or not")
temp=int(num)
count = len(num)
print(count)
output=0
lists=[]
while temp > 0 :
    lists.append(temp%10)
    temp=int(temp/10)

for i in lists:
   output = int(output + pow(i,count))
  # print(output)

if(int(num) == output):
    print('{} is a armstrong number'.format(num))
else:
    print('{} is not a armstrong number'.format(num))

output:
    Enter the number to whelter it is armstrong number or not153
3
153 is a armstrong number


    

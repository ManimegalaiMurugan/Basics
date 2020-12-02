sum = 0
count = 0
while True:
    inp = input("Enter the number")
    if len(inp):
       sum =sum + int(inp)
       count =count +1
    else:
        break
avg = sum / count
print(avg)
a = [1,2,3]
b = [4,5,6]
c= a+b
print(len(c))

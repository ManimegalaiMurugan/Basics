s = input("enter a string to check if it has unique letter")
s1 = list(s)
print(s1)
t = ''
for i in s1:
    if i in t:
        pass
    else:
        t = t + i
if len(t) == len(s):
    print('Yes')
else:
    print("no")
    

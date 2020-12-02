lists = [1,2,3,4]
dicts = {}

for iter in lists:
    dicts[iter] =pow(iter,3)
for i in dicts:
    print(i,dicts[i])

==================================
list1 = [1, 2, 5, 6] 

res = [(val, pow(val, 3)) for val in list1] 
 
print(res) 

=================================

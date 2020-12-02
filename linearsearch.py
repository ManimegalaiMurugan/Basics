lists = [10,20,40,30,70,60,50,78]
search = int(input("Enter a number to search"))
pos = -1
for i in range(0,len(lists)):
    if search == lists[i]:
        pos = i
print("position of search element {} ".format(pos))

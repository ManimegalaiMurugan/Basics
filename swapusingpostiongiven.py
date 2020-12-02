lists =  [1, 2, 3, 4, 5]
pos1 = int(input("Enter the first position : "))
pos2 = int(input("Enter the second position : "))
lists[pos2-1],lists[pos1-1] = lists[pos1-1],lists[pos2-1]
print(lists)

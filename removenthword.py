lists = ["perfect", "plan", "perfect"]
word = input("Enter a word to remove ")
n = int(input("Enter a position to remove"))
count = 0
pos = 0
list1 = list()
if word in lists:
    for i in lists:
        if i == word:
            count = count + 1
            if count == n:
                del lists[pos]
                continue
        pos = pos+1
        
print(lists)







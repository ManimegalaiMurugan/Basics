count = dict()
line = input("enter a sentence")
words = line.split()
for word in words:
    count[word] = count.get(word,0)+1
print(count)

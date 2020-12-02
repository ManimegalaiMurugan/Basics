para = open('para.txt')
dictionary = dict()
paras = para.read()
words = paras.split()
for word in words:
    dictionary[word] = dictionary.get(word,0) + 1
print(dictionary)
max = -1
wor = None
for k,v in dictionary.items():
    print(k,v)
    if v > max :
         max = v
         wor = k


print('Done',wor,max)
    

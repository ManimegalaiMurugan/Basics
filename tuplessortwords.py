parag = open('para.txt')
dictionary = {}
words = list()
for  iter in parag:
    words = iter.split()
    for wor in words:
        dictionary[wor] =dictionary.get(wor,0) + 1

for dicti in dictionary:
    print(dicti,dictionary[dicti])

listsort=[]

for k,v in dictionary.items():
    listsort.append( (v,k) )
finallist = sorted(listsort,reverse = True)
for sor in finallist:
    print(sor)



fread = open('filecopy.txt')
fappend = open('files.txt','w')
count = 0
for i in fread:
     count = count + 1
     if count % 2 != 0:
        fappend.write(i)
print(fappend)
fread.close()
fappend.close()
fopen = open('files.txt')
print(fopen.read())
fopen.close()


==================================================================


fread = open('filecopy.txt')
fappend = open('files.txt','w')
cont = fread.readlines()
print(type(cont)) # <class 'list'>
for i in range(0,len(cont)):
     if i % 2 == 0:
        fappend.write(cont[i])
print(fappend)
fread.close()
fappend.close()
fopen = open('files.txt','r')
print(fopen.read())
fopen.close()

ffile = open('demmo.txt')
for i in ffile:
    list = i.split('com ')
    week = list[1].split()
    print(week[0])

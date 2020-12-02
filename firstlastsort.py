lists = [10,23,45,6,7]
temp = lists[0]
lists[0] = lists[-1]
lists[-1]=temp
for iter in lists:
    print(iter)

========================

lists = [10,23,45,6,7]
lists[0],lists[-1]=lists[-1],lists[0]
for iter in lists:
    print(iter)

========================

lists = [10,23,45,6,7]
done = lists[-1],lists[0]
lists[0],lists[-1]=done
for iter in lists:
    print(iter)

========================

lists = [10,23,45,6,7]
first = lists.pop(-1)
last = lists.pop(0)

lists.insert(0,first)
lists.append(last)

for iter in lists:
    print(iter)

=========================



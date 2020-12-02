unsorted_file_name = 'C:/Users/Mohan/sample/test.txt'
sorted_file_name = 'C:/Users/Mohan/sample/animals-sorted.txt'
animals = []
try:
        animals_file=open(unsorted_file_name)
        for line in animals_file:
            animals.append(line)
            animals.sort()
            
except:
    print('Could not open {}.'.format(unsorted_file_name))
try:
    with open(sorted_file_name, 'w') as animals_sorted_file:
        for animal in animals:
            animals_sorted_file.write(animal)
except:
    print('Could not open {}{}.'.format(sorted_file_name))
    
for i in animals :
        print(i)
try:
   edited=open(animals_sorted_file,'r')
   edited_context=edited.read()
   for s in edited_context :
        print(s.rstrip())
except:
        print("fine by me")

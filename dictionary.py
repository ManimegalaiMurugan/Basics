people = {
    'geetha': ' used to tell lot of lies ',
    'deepak':' dont know what to say ',
    'arthi':" used to make fun out of others"
}

for name,story in people.items() :
    print('{} : {}'.format(name,story))
======================================

def display_facts(facts):

for fact in facts:
print('{}: {}'.format(fact, facts[fact]))
print()
facts = {
'Jason': 'Can fly an airplane.',
'Jeff': 'Is afraid of clowns.',
'David': 'Plays the piano.'
}
display_facts(facts)
facts['Jeff'] = 'Is afraid of heights.'
facts['Jill'] = 'Can hula dance.'
display_facts(facts)

==============================================
airport = [ ('chennai','ch001'),('karnataka','kr001'),('kerala','kr001') ]

for (airport_name,airport_code) in airport:
    print(' the code for {} is {} '.format(airport_name,airport_code))
==============================================
airports = [
("O’Hare International Airport", 'ORD'),
('Los Angeles International Airport', 'LAX'),
('Dallas/Fort Worth International Airport', 'DFW'),
('Denver International Airport', 'DEN')
]
for (airport, code) in airports:
print('The code for {} is {}.'.format(airport, code))
=================================================
with open("C:/Users/Mohan/sample/test.txt") as testing:
    #length = len(testing_content)
    le = 0
    for i in testing:
        le = le + 1
        print(le, ".",i.rstrip())
=================================================

unsorted_file_name = 'C:/Users/Mohan/sample/test.txt'
sorted_file_name = 'C:/Users/Mohan/sample/animals-sorted.txt'
animals = []
try:
    with open(unsorted_file_name) as animals_file:
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
    print('Could not open {}.'.format(sorted_file_name))
    
for i in animals:
    print(i)
===================================================

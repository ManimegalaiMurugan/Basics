
def catmethod(cat_text):
    length = len(cat_text)
    if len != 0:
        print('                 {}'.format('_' * length))
        print('               < {} >'.format(cat_text))
        print('                 {}'.format('-' * length))
        print('                /')
        print('  /\_/\        /')
        print('( o . o )')
        print('  > ^ < ')
    else:
        pass


def main():
    text = input('What would you like the cat to say? ')
    catmethod(text)
if __name__ == '__main__':
    main()
======================================   
import module
def main():
    module.catmethod('Feed me.')
    module.catmethod('Pet me.')
    module.catmethod('Purr. Purr.')

if __name__ == '__main__':
    main()

======================================

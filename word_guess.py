Word = input("Enter a word to guess : ")
output = [" "]*len(Word)

    
def single_letter(letter):
    
    if len(letter) == 1:
        return True
    else:
        return False


def word_check(letter):
    counts = Word.count(letter)
    if counts:
        print(" count of letter '{}' is : {}".format(letter,counts))
    return counts

def find_position(letter,Word,output):
    
    for i in range(len(Word)):
        if letter == Word[i]:
            output[i]= letter
            
        else:
            pass
    
    return output




for i in range(12):
    letter = input("Enter a letter : ")
    has_letter = single_letter(letter)
    if has_letter == 1:
        counts = word_check(letter)
        output = find_position(letter,Word,output)
    else:
       print("enter a single letter !!")
   
    tring=""
    for iter in output:
        tring = tring + iter
   
    if tring == Word:
        print("Congratulation !!! You found the word ")
        break
    else :
        pass
else:
    print("Better luck !!!")




          
    
   
 

            
    


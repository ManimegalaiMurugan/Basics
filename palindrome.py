s = input("Enter the string to check it is palindrome or not : ")
out = s[::-1]
if s == out:
    print('Yes')
else:
    print('no')

=====================================================

s = input("Enter the string to check it is palindrome or not : ")
def ispalindrome(s):
    for iter in range(0,int(len(s)/2)):
        if s[iter] != s[len(s)-iter-1]:
            return False
        else :
            return True

if ispalindrome(s):
    print('yes')
else:
    print("no")
=======================================================
s = input("Enter the string to check it is palindrome or not : ")

rev = ''.join(reversed(s))

if s == rev:
    print('yes')
else :
    print('no')
================================================





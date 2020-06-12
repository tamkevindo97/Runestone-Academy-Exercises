import string

def reverse(string):
    rev = ""
    for i in range(1,len(string)+1):
        if len(rev) == len(string):
            print(rev)
        else:
            rev = rev + string[-i]
    return rev

def palindrome(s):
    mod1 = s.replace(" ", "")
    mod2 = mod1.lower()
    mod3 = mod2.translate(str.maketrans('', '', string.punctuation))
    if reverse(mod3) == mod3:
        print("'", s , "'", "is a palindrome")
    else:
        print("'", s , "'", "is not a palindrome")


palindrome("madam i'm adam")
palindrome("madam i'm kevin")

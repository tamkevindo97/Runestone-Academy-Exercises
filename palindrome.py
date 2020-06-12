import string

# Returns the reverse of a string
def reverse(string):
    rev = ""
    for i in range(1, len(string)+1):
        if len(rev) == len(string):
            print(rev)
        else:
            rev = rev + string[-i]
    return rev

# Modifies string to remove spaces and punctuation before comparing with reverse
def palindrome(s):
    mod1 = s.replace(" ", "") # Remove all spaces from string
    mod2 = mod1.lower() # Make all letters in string lower case
    mod3 = mod2.translate(str.maketrans('', '', string.punctuation)) # Remove all punctuation from string
    if reverse(mod3) == mod3: 
        print("'", s, "'", "is a palindrome!")
    else:
        print("'", s, "'", "is not a palindrome.")

# Test cases
palindrome("Madam I'm Adam")
palindrome("Madam I'm Kevin")
palindrome("Live not on evil")

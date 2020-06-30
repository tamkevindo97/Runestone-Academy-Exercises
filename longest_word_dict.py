import string

def longest_word(text):
    text.translate(str.maketrans('', '', string.punctuation))
    list_text = list(text.split())
    dictionary = {}
    for aChar in list_text:
        dictionary.update({aChar: len(aChar)})

    max_key = max(dictionary, key=dictionary.get)
    print(dictionary)
    return max_key

def main():
    text = input("Enter a sentence to see which word is longest: ")
    print(longest_word(text))
main()
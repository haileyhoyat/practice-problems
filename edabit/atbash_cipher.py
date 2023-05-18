#https://edabit.com/challenge/MGALfBAXhXqqdFyqo

import string
alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
digits = list(string.digits)
punctuation = list(string.punctuation)
whitespace = list(string.whitespace)

def atbash(string):

    #go through each character in the string
    #if character exists in alphabet_lower or alphabet_upper, conduct algorthm to find mirror character
    #else, print chacter as is

    new_string = ""
    index = 0
    for character in string:
        if character in alphabet_lower:
            index = alphabet_lower.index(character)
            new_string += alphabet_lower[-1-index]
        elif character in alphabet_upper:
            index = alphabet_upper.index(character)
            new_string += alphabet_upper[-1-index]
        else:
            new_string += character

    return new_string

if __name__ == "__main__":
    
    word = "apple"
    word2 = ("Hello world!")
    word3 = ("Christmas is the 25th of December")
    print(atbash(word))
    print(atbash(word2))
    print(atbash(word3))



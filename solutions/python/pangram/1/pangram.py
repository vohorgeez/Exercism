def is_pangram(sentence):
    yes_it_is = True
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in alphabet:
        if letter not in sentence.lower():
            yes_it_is = False
    return yes_it_is
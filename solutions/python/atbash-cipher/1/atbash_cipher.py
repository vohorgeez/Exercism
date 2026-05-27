alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

def encode(plain_text):
    word = 0
    ciphered = ""
    for char in plain_text:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            ciphered += alphabet[-index-1]
            word = (word + 1) % 5
        elif char in numbers:
            ciphered += char
            word = (word + 1) % 5
        else:
            continue
        if word == 0:
            ciphered += " "
    return ciphered.strip()


def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(" ", "")
    decoded = ""
    for char in ciphered_text:
        if char in alphabet:
            index = alphabet.index(char.lower())
            decoded += alphabet[-index-1]
        if char in numbers:
            decoded += char
    return decoded
def rotate(text, key):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext = ""
    for char in text:
        if char.lower() in chars:
            index = chars.find(char.lower())
            new_char = chars[(index + key) % 26]
            if char.isupper():
                new_char = new_char.upper()
            ciphertext += new_char
        else:
            ciphertext += char
    return ciphertext
def translate(text):
    words = text.split()
    vowels = ["a", "e", "i", "o", "u"]
    translated = ""
    for word in words:
        if (word[0] in vowels) or (word[0:2] == "xr") or (word[0:2] == "yt"):
            new_word = word + "ay"
        elif (word[0] not in vowels) and (word[0].isalpha()):
            i=0
            consonants=""
            while (word[i] not in vowels) and (word[i].isalpha()):
                consonants += word[i].lower()
                if (word[i+1].lower() == "y"):
                    i += 1
                    break
                if (word[i].lower() == "q") and (word[i+1].lower() == "u"):
                    consonants += "u"
                    i += 2
                    break
                i += 1
            new_word = word[i:] + consonants + "ay"
        translated += new_word + " "
    return translated[:-1]
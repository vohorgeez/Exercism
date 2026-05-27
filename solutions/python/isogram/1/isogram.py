def is_isogram(string):
    yes_it_is = True
    checked_letters = []
    for letter in string:
        if (letter.lower() in checked_letters) and (letter.isalpha()):
            yes_it_is = False
        checked_letters.append(letter.lower())
    return yes_it_is

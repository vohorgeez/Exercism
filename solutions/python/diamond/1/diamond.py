def rows(letter): 
    letter_value = ord(letter.upper()) - 64
    side_square_value = (letter_value*2) - 1
    typical_row = []
    result = []
    for i in range(side_square_value):
        if i < letter_value:
            typical_row.append(chr(letter_value + 64 - i))
        else:
            typical_row.append(chr(letter_value + 64 - (side_square_value - i - 1)))
    for i in range(side_square_value):
        row = ""
        for letter in typical_row:
            if i < letter_value:
                if letter != chr(65+i):
                    row += " "
                else:
                    row += letter
            else:
                if letter != chr(64+side_square_value-i):
                    row += " "
                else:
                    row += letter
        result.append(row)
    return result
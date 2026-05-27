def is_valid(isbn):
    d = []
    for char in isbn:
        if char == '-':
            continue
        elif char.isnumeric():
            d.append(int(char))
        elif len(d) == 9 and char == 'X':
            d.append(10)
        else:
            return False
    if len(d) != 10:
        return False
    sum = 0
    for i in range(10):
        sum += d[i]*(10-i)
    return sum % 11 == 0
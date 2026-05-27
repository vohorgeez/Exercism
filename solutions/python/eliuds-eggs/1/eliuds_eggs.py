def egg_count(display_value):
    binary = bin(display_value)[1:]
    count = 0
    for digit in binary:
        if digit == '1':
            count += 1
    return count
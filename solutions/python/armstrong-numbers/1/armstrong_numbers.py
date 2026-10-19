def is_armstrong_number(number):
    stringified = str(number)
    digits = []
    for digit in stringified:
        digits.append(int(digit))
    power = len(digits)
    sum = 0
    for digit in digits:
        sum += digit**power
    return number == sum
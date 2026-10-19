def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2 :
        raise ValueError("output base must be >= 2")
    if len(digits) == 0:
        return [0]
    base10 = 0
    power = len(digits) - 1
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        base10 += digit * (input_base**power)
        power -= 1
    based = []
    if base10 == 0:
        return [0]
    while base10 != 0:
        based.insert(0, base10 % output_base)
        base10 = base10 // output_base
    return based
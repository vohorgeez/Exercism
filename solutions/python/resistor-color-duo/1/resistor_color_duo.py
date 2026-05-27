def value(colors):
    all_colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    digits = []
    for color in colors:
        digits.append(all_colors.index(color))
    number = digits[0]*10 + digits[1]
    return number
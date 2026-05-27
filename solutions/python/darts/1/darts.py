def score(x, y):
    circle = x**2 + y**2
    if circle <= 1:
        return 10
    elif circle <= 5**2:
        return 5
    elif circle <= 10**2:
        return 1
    else:
        return 0
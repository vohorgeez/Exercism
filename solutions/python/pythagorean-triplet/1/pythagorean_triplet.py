def triplets_with_sum(number):
    output = []
    for a in range(1, number):
        if number**2 % (2*a - 2*number) == 0:
            b = int(number + (number**2 / (2*a - 2*number)))
            c = number - a - b
            if a<b<c and a+b+c==number and a**2+b**2==c**2:
                output.append([a,b,c])
    return output
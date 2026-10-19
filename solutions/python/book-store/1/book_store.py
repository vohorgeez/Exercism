def total(basket):
    series = {
        "I":basket.count(1),
        "II":basket.count(2),
        "III":basket.count(3),
        "IV":basket.count(4),
        "V":basket.count(5)
    }

    to_delete = []

    for volume in series.keys():
        if series[volume] == 0:
            to_delete.append(volume)
    for item in to_delete:
        series.pop(item)

    to_delete = []
    discounts = []

    price = 0

    while series:
        minimum_repetition = min(series.values())
        to_delete = []
        if len(series) == 5:
            for i in range(minimum_repetition):
                discounts.append(5)
            for volume in series.keys():
                series[volume] -= minimum_repetition
                if series[volume] == 0:
                    to_delete.append(volume)
            for item in to_delete:
                series.pop(item)
        elif len(series) == 4:
            for i in range(minimum_repetition):
                discounts.append(4)
            for volume in series.keys():
                series[volume] -= minimum_repetition
                if series[volume] == 0:
                    to_delete.append(volume)
            for item in to_delete:
                series.pop(item)
        elif len(series) == 3:
            for i in range(minimum_repetition):
                discounts.append(3)
            for volume in series.keys():
                series[volume] -= minimum_repetition
                if series[volume] == 0:
                    to_delete.append(volume)
            for item in to_delete:
                series.pop(item)
        elif len(series) == 2:
            for i in range(minimum_repetition):
                discounts.append(2)
            for volume in series.keys():
                series[volume] -= minimum_repetition
                if series[volume] == 0:
                    to_delete.append(volume)
            for item in to_delete:
                series.pop(item)
        elif len(series) == 1:
            for i in range(minimum_repetition):
                discounts.append(1)
            for volume in series.keys():
                series[volume] -= minimum_repetition
                if series[volume] == 0:
                    to_delete.append(volume)
            for item in to_delete:
                series.pop(item)

    number_of_replacements = min(discounts.count(5), discounts.count(3))
    for i in range(number_of_replacements):
        discounts.remove(5)
        discounts.remove(3)
        discounts.append(4)
        discounts.append(4)
    for nuplet in discounts:
        if nuplet == 5:
            price += 3000
        if nuplet == 4:
            price += 2560
        if nuplet == 3:
            price += 2160
        if nuplet == 2:
            price += 1520
        if nuplet == 1:
            price += 800
    return price
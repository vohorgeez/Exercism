def resistor_label(colors):
    color_bands = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    tolerance_bands = {
        "grey": "±0.05%",
        "violet": "±0.1%",
        "blue": "±0.25%",
        "green": "±0.5%",
        "brown": "±1%",
        "red": "±2%",
        "gold": "±5%",
        "silver": "±10%"
    }
    value_1 = color_bands.index(colors[0])
    value_2 = color_bands.index(colors[1]) if len(colors) >= 2 else None
    value_3 = color_bands.index(colors[2]) if len(colors) == 5 else None
    if 3 <= len(colors) < 5:
        multiplier = color_bands.index(colors[2])
    elif len(colors) == 5:
        multiplier = color_bands.index(colors[3])
    else:
        multiplier = 0
    value = value_1
    if value_2 is not None:
        value = value * 10 + value_2
        if value_3 is not None:
            value = value *10 + value_3
    value = value * (10**multiplier)

    if value >= 1000000000:
        value = value / 1000000000
        unit = "gigaohms"
    elif value >= 1000000:
        value = value / 1000000
        unit = "megaohms"
    elif value >= 1000:
        value = value / 1000
        unit = "kiloohms"
    else:
        unit = "ohms"

    value = int(value) if value.is_integer() else value

    tolerance = tolerance_bands[colors[-1]] if len(colors) >= 4 else None

    if len(colors) < 4:
        return str(value) + " " + unit
    else:
        return str(value) + " " + unit + " " + tolerance
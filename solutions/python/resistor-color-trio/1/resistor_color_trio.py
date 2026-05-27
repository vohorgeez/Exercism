def label(colors):
    all_colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    ohms = (all_colors.index(colors[0])*10 + all_colors.index(colors[1])) * 10**all_colors.index(colors[2])
    if ohms >= 1000000000:
        ohms = ohms // 1000000000
        return str(ohms) + " gigaohms"
    elif ohms >= 1000000:
        ohms = ohms // 1000000
        return str(ohms) + " megaohms"
    elif ohms >= 1000:
        ohms = ohms // 1000
        return str(ohms) + " kiloohms"
    return str(ohms) + " ohms"
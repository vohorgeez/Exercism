def recite(start, take=1):
    numbers = ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    lyrics = []
    for i in range(start, start-take, -1):
        lyrics.append(f"{numbers[i].title()} green bottle{'s' if i > 1 else ''} hanging on the wall,")
        lyrics.append(f"{numbers[i].title()} green bottle{'s' if i > 1 else ''} hanging on the wall,")
        lyrics.append("And if one green bottle should accidentally fall,")
        lyrics.append(f"There'll be {numbers[i-1]} green bottle{'' if i-1 == 1 else 's'} hanging on the wall.")
        if i != start-take+1:
            lyrics.append("")
    return lyrics
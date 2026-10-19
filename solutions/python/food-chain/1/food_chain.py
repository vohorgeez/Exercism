def recite(start_verse, end_verse):
    animal = [None, 'fly', 'spider', 'bird', 'cat', 'dog', 'goat', 'cow', 'horse']
    exclamation = {
        'fly':"I don't know why she swallowed the fly. Perhaps she'll die.",
        'spider':"It wriggled and jiggled and tickled inside her.",
        'bird': "How absurd to swallow a bird!",
        'cat': "Imagine that, to swallow a cat!",
        'dog': "What a hog, to swallow a dog!",
        'goat': "Just opened her throat and swallowed a goat!",
        'cow': "I don't know how she swallowed a cow!",
        'horse': "She's dead, of course!"
    }
    lyrics = []
    for i in range(start_verse, end_verse+1):
        lyrics.append(f"I know an old lady who swallowed a {animal[i]}.")
        lyrics.append(exclamation[animal[i]])
        if i == 8:
            break
        if 1 < i <= 7:
            j = i
            while j != 1:
                lyrics.append(f"She swallowed the {animal[j]} to catch the {animal[j-1]}{" that wriggled and jiggled and tickled inside her" if j-1 == 2 else ''}.")
                j -= 1
        if i > 1:
            lyrics.append(exclamation['fly'])
        if i != end_verse:
            lyrics.append("")
    return lyrics
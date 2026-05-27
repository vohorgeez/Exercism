def recite(start_verse, end_verse):
    which_day = [None, 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    how_many = [None, 'a', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    presents = [
        None, # too bad
        'Partridge in a Pear Tree',
        'Turtle Doves',
        'French Hens',
        'Calling Birds',
        'Gold Rings',
        'Geese-a-Laying',
        'Swans-a-Swimming',
        'Maids-a-Milking',
        'Ladies Dancing',
        'Lords-a-Leaping',
        'Pipers Piping',
        'Drummers Drumming'
    ]
    lyrics = []
    for i in range(start_verse, end_verse+1):
        verse = f"On the {which_day[i]} day of Christmas my true love gave to me: {how_many[i]} {presents[i]}"
        if i != 1:
            j = i - 1
            while j != 0:
                verse += ", "
                if j == 1:
                    verse += "and "
                verse += f"{how_many[j]} {presents[j]}"
                j -= 1
        verse += "."
        lyrics.append(verse)
    return lyrics
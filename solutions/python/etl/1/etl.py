def transform(legacy_data):
    data = {}
    for points in legacy_data.keys():
        for letter in legacy_data[points]:
            data[letter.lower()] = points
    sorted_data = dict(sorted(data.items()))
    return sorted_data
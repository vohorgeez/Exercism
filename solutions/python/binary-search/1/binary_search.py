def find(search_list, value):
    search_list.sort()
    length = len(search_list)
    index = length // 2
    if search_list == []:
        raise ValueError("value not in array")
    while search_list[index] != value:
        if index == 0 or index == len(search_list) - 1:
            raise ValueError("value not in array")
        if search_list[index] > value:
            length //= 2
            index = length // 2
        else:
            length //= 2
            index += length // 2 if length != 0 else 1
    return index
def annotate(garden):
    if not isinstance(garden, list):
        raise ValueError("The board is invalid with current input.")

    if len(garden) == 0:
        return []

    width = len(garden[0])
    height = len(garden)

    for row in garden:
        if len(row) != width:
            raise ValueError("The board is invalid with current input.")
        for char in row:
            if char not in (' ', '*'):
                raise ValueError("The board is invalid with current input.")

    new_garden = []

    for i in range(height):      # ← height : nombre de lignes
        new_row = ''
        for j in range(width):   # ← width  : nombre de colonnes
            if garden[i][j] == '*':
                new_row += '*'
            else:
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < height and 0 <= nj < width:
                            if garden[ni][nj] == '*':
                                count += 1
                new_row += str(count) if count > 0 else ' '
        new_garden.append(new_row)

    return new_garden
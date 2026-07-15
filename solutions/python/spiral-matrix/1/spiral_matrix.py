def spiral_matrix(size):
    matrix = [[None] * size for _ in range(size)]
    right = True
    down = False
    left = False
    up = False
    coord = {"line": 0, "col": 0}
    for i in range(1, size**2+1):
        matrix[coord["line"]][coord["col"]] = i
        if right:
            if coord["col"] >= size-1 or matrix[coord["line"]][coord["col"] + 1] is not None:
                right, down = False, True
                coord["line"] += 1
            else:
                coord["col"] += 1
        elif down:
            if coord["line"] >= size-1 or matrix[coord["line"] + 1][coord["col"]] is not None:
                down, left = False, True
                coord["col"] -= 1
            else:
                coord["line"] += 1
        elif left:
            if coord["col"] == 0 or matrix[coord["line"]][coord["col"] - 1] is not None:
                left, up = False, True
                coord["line"] -= 1
            else:
                coord["col"] -= 1
        elif up:
            if coord["line"] == 0 or matrix[coord["line"] - 1][coord["col"]] is not None:
                up, right = False, True
                coord["col"] += 1
            else:
                coord["line"] -= 1
    return matrix
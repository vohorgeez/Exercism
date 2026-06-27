def saddle_points(matrix):
    great_spots = []
    if matrix == []:
        return great_spots
    for row in matrix:
        if len(matrix[0]) != len(row):
            raise ValueError("irregular matrix")
    for i in range(len(matrix)):
        tallest_in_a_row = max(matrix[i])
        for j in range(len(matrix[i])):
            smallest_in_a_column = min(matrix[k][j] for k in range(len(matrix)))
            if matrix[i][j] == tallest_in_a_row and matrix[i][j] == smallest_in_a_column:
                great_spots.append({"row": i+1, "column": j+1})
    return great_spots
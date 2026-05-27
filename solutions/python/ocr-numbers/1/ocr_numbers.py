def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    for line in input_grid:
        if len(line) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")
        
    output = ""
    for i in range(0, len(input_grid), 4):
        if i != 0:
            output += ","
        for j in range(0, len(input_grid[i]), 3):
            if input_grid[i][j:j+3] == "   " and input_grid[i+1][j:j+3] == "  |" and input_grid[i+2][j:j+3] == "  |":
                output += "1"
            elif input_grid[i][j:j+3] == " _ " and input_grid[i+1][j:j+3] == " _|" and input_grid[i+2][j:j+3] == "|_ ":
                output += "2"
            elif input_grid[i][j:j+3] == " _ " and input_grid[i+1][j:j+3] == " _|" and input_grid[i+2][j:j+3] == " _|":
                output += "3"
            elif input_grid[i][j:j+3] == "   " and input_grid[i+1][j:j+3] == "|_|" and input_grid[i+2][j:j+3] == "  |":
                output += "4"
            elif input_grid[i][j:j+3] == " _ " and input_grid[i+1][j:j+3] == "|_ " and input_grid[i+2][j:j+3] == " _|":
                output += "5"
            elif input_grid[i][j:j+3] == " _ " and input_grid[i+1][j:j+3] == "|_ " and input_grid[i+2][j:j+3] == "|_|":
                output += "6"
            elif input_grid[i][j:j+3] == " _ " and input_grid[i+1][j:j+3] == "  |" and input_grid[i+2][j:j+3] == "  |":
                output += "7"
            elif input_grid[i][j:j+3] == " _ " and input_grid[i+1][j:j+3] == "|_|" and input_grid[i+2][j:j+3] == "|_|":
                output += "8"
            elif input_grid[i][j:j+3] == " _ " and input_grid[i+1][j:j+3] == "|_|" and input_grid[i+2][j:j+3] == " _|":
                output += "9"
            elif input_grid[i][j:j+3] == " _ " and input_grid[i+1][j:j+3] == "| |" and input_grid[i+2][j:j+3] == "|_|":
                output += "0"
            else:
                output += "?"

    return output
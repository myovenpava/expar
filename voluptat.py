def move_left(matrix, row, col):
    if col - 1 < 0 or matrix[row][col - 1] == "X":
        return row, col
    else:
        return row, col - 1

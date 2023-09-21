import sys

rows, columns = list(map(int, input().split(", ")))

matrix = []
submatrix = []
sum_submatrix = -sys.maxsize

for row in range(rows):
    cols = list(map(int, input().split(", ")))
    matrix.append(cols)

for row in range(rows):

    for col in range(columns):
        if row+1 < rows and col+1 < columns:
            square = [matrix[row][col], matrix[row][col+1], matrix[row+1][col], matrix[row+1][col+1]]
            if sum(square) > sum_submatrix:
                submatrix = [[square[0], square[1]], [square[2], square[3]]]
                sum_submatrix = sum(square)

[print(' '.join([str(col) for col in row])) for row in submatrix]
print(sum_submatrix)





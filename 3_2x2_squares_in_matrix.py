rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for x in range(rows)]
counter = 0

for row in range(rows -1):
    for col in range(cols - 1):
        current_symbol = matrix[row][col]
        if matrix[row][col + 1] == current_symbol and matrix[row + 1][col] == current_symbol  and matrix[row + 1][col + 1] == current_symbol:
            counter += 1

print(counter)


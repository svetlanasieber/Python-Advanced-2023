# rows, columns = (int(x) for x in input().split())
# matrix = [input().split() for i in range(rows)]
# print(matrix)
# counter = 0
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
#             counter += 1
#



rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for x in range(rows)]
counter = 0

for row in range(rows -1):
    for col in range(cols - 1):
        current_symbol = matrix[row][col]
        if matrix[row][col + 1] == current_symbol and matrix[row + 1][col] == current_symbol  and matrix[row + 1][col + 1] == current_symbol:
            counter += 1

print(counter)


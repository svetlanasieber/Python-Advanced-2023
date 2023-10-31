# row, col = map(int, input().split(', '))
# matrix = [map(int, input().split(', ') for col in range(col)] for row in range(row)]
#
#
#
#
#
matrix = []
row, col = map(int, input().split(', '))

for i in range(row):

    row_nums = list(map(int, input().split(', ')))
    matrix.append(row_nums)

suma = sum([sum(el) for el in matrix])
print(suma)





# def read_matrix():
#     row, col = map(int, input().split(', '))
#     current_matrix = []
#
#     for i in range(row):
#         row_nums = list(map(int, input().split(', ')))
#         current_matrix.append(row_nums)
#     return current_matrix
#
#
# matrix = read_matrix()
# print(matrix)
matrix = [list(map(int, input().split(', '))) for x in range(int(input()))]
matrix2 = [[int(el) for el in input().split(', ')] for _ in range(int(input()))] 

print(matrix)
new_matrix = []
for row in matrix:
    for num in row:
        new_matrix.append(num)
print(new_matrix)

result = [num for num in matrix for num in row]

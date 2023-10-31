rows = int(input())
matrix = []

for i in range(rows):
    current_row = [int(el) for el in input().split(', ') if int(el) % 2 ==0]
    matrix.append(current_row)
    # cols = list(map(int, input().split(', ')))
print(matrix)




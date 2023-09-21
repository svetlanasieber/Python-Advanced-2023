from collections import deque

rows, columns = list(map(int, input().split()))

snake = input()

matrix = []

index_snake = 0

for row in range(rows):

    result = deque()

    for col in range(columns):

        if index_snake == len(snake):
            index_snake = 0

        if row % 2 == 0:
            result.append(snake[index_snake])

        else:
            result.appendleft(snake[index_snake])

        index_snake += 1

    matrix.append(list(result))
    print("".join(result))



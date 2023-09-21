from string import ascii_letters

letters = dict(zip([ord(c)%32 for c in ascii_letters], ascii_letters.lower()))

rows, columns = list(map(int, input().split()))

matrix = []

for row in range(rows):

    cols = []

    for col in range(columns):
        column = letters[row+1] + letters[col+row+1] + letters[row+1]
        cols.append(column)

    matrix.append(cols)
    print(' '.join(cols))



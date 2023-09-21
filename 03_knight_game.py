board_size = int(input()) # rows and columns

removed_knights = 0

matrix = [list(input()) for row in range(board_size)]

knight = "K"


def check_index(row, col):
    if 0 <= row < board_size and 0 <= col < board_size:
        return True
    return False


moves = {
    "top_left": (-2, -1),
    "middle_left": (-1, -2),
    "top_right": (-2, 1),
    "middle_right": (-1, 2),

    "bottom_left": (2, -1),
    "middle_bottom_left": (1, -2),
    "bottom_right": (2, 1),
    "middle_bottom_right": (1, 2)
}

knights = {}


def find_best_knight():
    global knights
    knights = {}

    number_of_good_knights = 0

    for row in range(board_size):

        for col in range(board_size):

            if matrix[row][col] == knight:

                for m_row, m_col in moves.values():
                    knight_row, knight_col = row + m_row, col + m_col

                    if check_index(knight_row, knight_col):
                        if matrix[knight_row][knight_col] == knight:
                            number_of_good_knights += 1
                            if f"{row} {col}" not in knights.keys():
                                knights[f"{row} {col}"] = 1

                            else:
                                knights[f"{row} {col}"] += 1

    if number_of_good_knights == 0:
        return False
    return True


def remove_knight():
    global removed_knights

    best_knight = [-1, -1]
    best_knight_attacks = 0

    for m_knight, attacks in knights.items():
        if attacks > best_knight_attacks:
            best_knight[0], best_knight[1] = int(m_knight.split()[0]), int(m_knight.split()[1])
            best_knight_attacks = attacks

    if best_knight[0] >= 0 and best_knight[1] >= 0:
        matrix[best_knight[0]][best_knight[1]] = '0'
        removed_knights += 1


while True:

    if not find_best_knight():
        break

    remove_knight()

print(removed_knights)





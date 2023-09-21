numbers = list(map(int, input().split()))
number_indexes = set()
target_number = int(input())

for first_index in range(len(numbers)):

    for second_index in range(len(numbers)):

        if first_index != second_index and first_index not in number_indexes and second_index not in number_indexes \
                and numbers[first_index] + numbers[second_index] == target_number:

            print(f"{numbers[first_index]} + {numbers[second_index]} = {target_number}")
            number_indexes.add(first_index), number_indexes.add(second_index)
            break




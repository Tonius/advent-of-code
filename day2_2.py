def are_strings_equal_except_one_char(first, second):
    differing_indexes = []

    for index, chars in enumerate(zip(first, second)):
        first_char, second_char = chars

        if first_char != second_char:
            differing_indexes.append(index)

    return len(differing_indexes) == 1

def find_strings(box_ids):
    for first_box_id in box_ids:
        for second_box_id in box_ids:
            if first_box_id == second_box_id:
                continue

            if are_strings_equal_except_one_char(first_box_id, second_box_id):
                return first_box_id, second_box_id

with open('day2input.txt') as input_file:
    box_ids = [line for line in input_file]

first_box_id, second_box_id = find_strings(box_ids)

print(first_box_id, second_box_id)

def get_count_of_char_in_string(string, char):
    return len([c for c in string if c == char])

def string_has_n_of_any_char(string, amount):
    seen_chars = []

    for char in string:
        if char in seen_chars:
            continue

        seen_chars.append(char)

        count = get_count_of_char_in_string(string, char)

        if count == amount:
            return True

    return False

input_file = open('day2input.txt')

two_count = 0
three_count = 0

for box_id in input_file:
    if string_has_n_of_any_char(box_id, 2):
        two_count += 1

    if string_has_n_of_any_char(box_id, 3):
        three_count += 1

checksum = two_count * three_count

print(checksum)

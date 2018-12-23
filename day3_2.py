def parse_claim_string(claim_string):
    claim_id, _, coords, size = claim_string.split(' ')
    x, y = coords[:-1].split(',')
    width, height = size.split('x')

    return claim_id, int(x), int(y), int(width), int(height)


with open('day3input.txt') as input_file:
    claim_strings = [line for line in input_file]

for claim_string in claim_strings:
    claimed_by_others = [
        [False for _ in range(1000)]
        for _ in range(1000)
    ]

    for other_claim_string in claim_strings:
        if other_claim_string == claim_string:
            continue

        claim_id, x, y, width, height = parse_claim_string(other_claim_string)

        for x_offset in range(width):
            for y_offset in range(height):
                claimed_by_others[x + x_offset][y + y_offset] = True

    claim_id, x, y, width, height = parse_claim_string(claim_string)

    overlaps = False

    for x_offset in range(width):
        if overlaps:
            break

        for y_offset in range(height):
            if overlaps:
                break

            if claimed_by_others[x + x_offset][y + y_offset]:
                print('{} overlaps'.format(claim_string))
                overlaps = True

    if not overlaps:
        print(claim_string)
        break

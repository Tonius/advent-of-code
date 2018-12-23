claims = [
    [0 for _ in range(1000)]
    for _ in range(1000)
]

input_file = open('day3input.txt')

for claim_string in input_file:
    claim_id, _, coords, size = claim_string.split(' ')

    x, y = coords[:-1].split(',')
    x = int(x)
    y = int(y)

    width, height = size.split('x')
    width = int(width)
    height = int(height)

    for x_offset in range(width):
        for y_offset in range(height):
            claims[x + x_offset][y + y_offset] += 1

at_least_two_count = 0

for row in claims:
    for claim in row:
        if claim >= 2:
            at_least_two_count += 1

print(at_least_two_count)

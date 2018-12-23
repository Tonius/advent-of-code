frequency = 0
seen = [frequency]

while True:
    with open('day1input.txt') as input_file:
        for line in input_file:
            frequency += int(line)

            if frequency in seen:
                print(frequency)
                exit(0)

            seen.append(frequency)

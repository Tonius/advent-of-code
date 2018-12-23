frequency = 0

input_file = open('day1input.txt')

for line in input_file:
    frequency += int(line)

print(frequency)

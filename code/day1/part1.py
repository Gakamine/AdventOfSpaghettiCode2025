import os

dial = 50
count = 0
with open(os.environ['INPUT_FILE'], 'r') as file:
    for line in file:
        line = line.strip()
        direction = line[0]
        steps = int(line[1:])
        if direction == 'L':
            dial = (dial - steps) % 100
        else:
            dial = (dial + steps) % 100
        if dial == 0:
            count += 1
print(count)
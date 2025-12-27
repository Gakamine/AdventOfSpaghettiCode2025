import os

count = 0
with open(os.environ['INPUT_FILE'], 'r') as file:
    for line in file:
        line = line.strip()
        joltage = [0 for x in range(0,12)]
        batteries = [x for x in line]
        index = 0
        offset = 11
        for i in range(0,12):
            batt_range = batteries[index:len(batteries)-offset]
            joltage[i] = max(batt_range)
            offset = offset - 1
            if index == 0:
                index = batteries.index(joltage[0]) + 1
            else:
                index = index + batt_range.index(joltage[i]) + 1
        count += int(''.join(joltage))
    print(count)
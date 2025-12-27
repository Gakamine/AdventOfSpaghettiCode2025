count = 0
with open('../inputs/day3/day3.txt', 'r') as file:
    for line in file:
        line = line.strip()
        batteries = list(line)
        tens = max(batteries[0:len(batteries)-1])
        unit = max(batteries[batteries.index(tens)+1:])
        number = int(str(tens) + str(unit))
        count += number
    print(count)
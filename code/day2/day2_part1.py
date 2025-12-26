with open('../inputs/day2/day2.txt', 'r') as file:
    count = 0
    for line in file:
        line = line.strip().split(",")
        for ranges in line:
            a, b = ranges.split("-")[0],ranges.split("-")[1]
            for i in range(int(a),int(b)+1):
                i = str(i)
                if len(i) % 2 == 0:
                    if i[0:len(i)//2] == i[len(i)//2:]:
                        count += int(i)
    print(count)
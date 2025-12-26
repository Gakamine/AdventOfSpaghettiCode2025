with open('../inputs/day2/day2.txt', 'r') as file:
    count = 0
    for line in file:
        line = line.strip().split(",")
        for ranges in line:
            a, b = ranges.split("-")[0],ranges.split("-")[1]
            for i in range(int(a),int(b)+1):
                i = str(i)
                for j in range(1,len(i)):
                    split = i.split(i[0:j])
                    if ''.join(split) == '':
                        count += int(i)
                        break
    print(count)
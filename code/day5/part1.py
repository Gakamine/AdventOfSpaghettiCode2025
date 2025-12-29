import os

count = 0
fresh_ids = []
with open(os.environ['INPUT_FILE'], 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            break
        fresh_ids.append([int(line.split("-")[0]),int(line.split("-")[1])])
    for line in file:
        for fresh_range in fresh_ids:
            if int(line.strip()) >= fresh_range[0] and int(line.strip()) <= fresh_range[1]:
                count += 1
                break
print(count)
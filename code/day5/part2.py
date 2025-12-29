import os

count = 0
fresh_ranges = []
with open(os.environ['INPUT_FILE'], 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            break
        start, end = map(int, line.split("-"))
        fresh_ranges.append([start, end])
fresh_ranges.sort(key=lambda x: x[0])
merged = []
for start, end in fresh_ranges:
    if not merged or merged[-1][1] < start:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)
for fresh_range in merged:
    count += fresh_range[1] - fresh_range[0]+1
print(count)
import os

with open(os.environ['INPUT_FILE'], 'r') as file:
    grid = [list(line.strip()) for line in file]
rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
count = 0
for y in range(rows):
    for x in range(cols):
        if grid[y][x] == "@":
            neighbor_count = 0
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == "@":
                    neighbor_count += 1
            if neighbor_count < 4:
                count += 1
print(count)
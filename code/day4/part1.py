import os

count = 0
with open(os.environ['INPUT_FILE'], 'r') as file:
    for line in file:
    print(count)
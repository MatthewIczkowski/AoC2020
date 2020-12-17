#Day 5: Binary Boarding
from projects.helpers import io
import statistics, math

passes = []

def add_to_arr(line):
    try:
        passes_item = line.strip('\n')
        passes.append(passes_item)
    except ValueError:
        return

def find_row(map):
    map = map.strip('RL')
    range = [0,127]
    for x in map:
        if x == 'F':
            range[1] = math.floor(statistics.median(range))
        else:
            range[0] = math.ceil(statistics.median(range))

    if map[-1] == "F":
        return range[0]
    else:
        return range[1]

def find_col(map):
    map = map.strip('FB')
    range = [0, 7]
    for x in map:
        if x == 'L':
            range[1] = math.floor(statistics.median(range))
        else:
            range[0] = math.ceil(statistics.median(range))

    if map[-1] == "R":
        return range[0]
    else:
        return range[1]

io.read_file_by_newline("day5.txt", add_to_arr)
highest_ID = -1
row = 0
col = 0
passes_sorted = []
for x in passes:
    row = find_row(x)
    col = find_col(x)
    current_ID = row*8+col
    passes_sorted.append(current_ID)
    if current_ID > highest_ID:
        highest_ID = current_ID

print('Highest ID: ', highest_ID)
passes_sorted = sorted(passes_sorted)
for i in range(0, len(passes_sorted)-1):
    if passes_sorted[i] != (passes_sorted[i+1] - 1):
        print("Open seat ID: ", passes_sorted[i]+1)





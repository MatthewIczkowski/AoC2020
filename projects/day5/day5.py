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
    #print(map)
    row = 0
    range = [0,127]

    for x in map:
        if x == 'F':
            range[1] = math.floor(statistics.median(range))
            #print(range)
        else:
            range[0] = math.ceil(statistics.median(range))
            #print(range)

    if map[-1] == "F":
        row = range[0]
    else:
        row = range[1]
    return row

def find_col(map):
    map = map.strip('FB')
    #print(map)
    col = 0
    range = [0, 7]

    for x in map:
        if x == 'L':
            range[1] = math.floor(statistics.median(range))
            # print(range)
        else:
            range[0] = math.ceil(statistics.median(range))
            # print(range)

    if map[-1] == "R":
        col = range[0]
    else:
        col = range[1]
    return col

io.read_file_by_newline("day5.txt", add_to_arr)
highest_ID = -1
row = 0
col = 0

for x in passes:
    #print(x)
    row = find_row(x)
    col = find_col(x)
    current_ID = row*8+col
    #print("Row: ", row)
    #print("Col: ", col)
    #print("Current ID: ", current_ID)
    if current_ID > highest_ID:
        highest_ID = current_ID

print('Highest ID: ', highest_ID)




#Day 3: Toboggan Trajectory

from projects.helpers import io

arr = []

def add_to_arr(line):
    try:
        arr_item = line
        arr.append(arr_item)
    except ValueError:
        return

io.read_file_by_newline("day3.txt", add_to_arr)

def is_tree(pos):
    if pos == "#":
        return 1
    else:
        return 0

#variables:
col = 0
row = 0
tree_count = 0

#restricted by movement over 3 columns and 1 row down
#step 1: start at arr[0][0] in upper lefthand corner of map

for row in range(0,len(arr)-1):
    # step 2: add 3 to column
    col += 3
    #print("Current col: ", col)
    #print("Current row: ", row)
    # Step 3: once last col is reached, subtract by number of columns to wrap back to beginning of row
    # step 4: check if current position is '#' or '.']
    if row >= len(arr)-1:
        print("No more rows, current row: ", row)
        break
    elif col >= len(arr[row])-1:
        print("Column attempt: ", col)
        print("Row attempt: ", row)
        col = col % (len(arr[row])-1)
        row += 1
        #print(col)
        #print(is_tree(arr[row][col]))
        tree_count += is_tree(arr[row][col])
        #print("Column > 32, column = ", col)
        #break
    else:
        row += 1
        #print(is_tree(arr[row][col]))
        tree_count += is_tree(arr[row][col])
    #move up 1 row to account for forloop increment
    #row -= 1

print("Tree count: ", tree_count)





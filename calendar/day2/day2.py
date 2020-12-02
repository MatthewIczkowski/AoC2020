#Day 2: Password Philsophy
from calendar.helpers import io

def add_to_arr(line):
    try:
        arr_item = int(line)
        arr.append(arr_item)
    except ValueError:
        return

def parse_line(line):
    range, letter, password = line.split(" ", 2)
    print("Range: " + range)
    print("Letter: " + letter[1])
    print("Password: " + password)
    return

def is_valid_pass(low, high, letter, password):
    count = 0
    for x in password:
        if x == letter:
            count+=1

    if count >= low and count <= high:
        return True
    else:
        return False

arr = []

io.read_file_by_newline("day1.txt", add_to_arr)



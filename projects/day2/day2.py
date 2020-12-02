#Day 2: Password Philsophy
from projects.helpers import io

arr = []

#When printing arr[0] w/o added blank line, first password is skipped
#Added blank line to day2.txt such that arr[0] prints first password in list
def add_to_arr(line):
    try:
        arr_item = line
        arr.append(arr_item)
    except ValueError:
        return

io.read_file_by_newline("day2.txt", add_to_arr)

#Need to figure out way to eliminate \n at end of password
#For some reason password.split() did not remove haning \n
#Current implementation with password[:-1] removes last character of final password entry
def parse_line(line):
    range, letter, password = line.split(" ", 2)
    low, high = range.split("-",1)
    parse_output = [int(low), int(high), letter[0], password[:-1]]
    return parse_output

def is_valid_pass(low, high, letter, password):
    count = 0
    for x in password:
        if x == letter:
            count+=1

    if count >= low and count <= high:
        return True
    else:
        return False

num_valid = 0
#Error being thrown after reaching the end of the dataset, attempting to run parse_line with invalid input
#Need to validate input before error is thrown at the end
for entry in arr:
    key = parse_line(entry)
    if is_valid_pass(key[0], key[1], key[2], key[3]) == True:
        num_valid+=1
    print(num_valid)



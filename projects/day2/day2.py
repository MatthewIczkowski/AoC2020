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
#For some reason password.strip() did not remove haning \n
#Current implementation with password[:-1] removes last character of final password entry
def parse_line(line):
    range, letter, password = line.split(" ", 2)
    low, high = range.split("-",1)
    password=password.strip()
    parse_output = [int(low), int(high), letter[0], password]
    return parse_output

#verifies if letter appears certain number of times in provided password
def is_valid_count(low, high, letter, password):
    count = 0
    for x in password:
        if x == letter:
            count+=1

    if count >= low and count <= high:
        return True
    else:
        return False

#verifies if letter appears one time in either of the pos provided number of times in provided password
#given position is not based on index zero, need to decrement given position to align with array index
#assume password does not contain letter in either position in set is_valid = False
def is_valid_pos(pos_1, pos_2, letter, password):
    pos_1-=1
    pos_2-=1
    is_valid = False

    if password[pos_1] == letter and password[pos_2] == letter:
        is_valid = False
    elif password[pos_1] == letter or password[pos_2] == letter:
        is_valid = True

    return is_valid


num_valid_count = 0
num_valid_pos = 0
#Error being thrown after reaching the end of the dataset, attempting to run parse_line with invalid input
#Currently reading up to len(arr)-1 to avoid error
#Ideally validate input before error is thrown at the end
for i in range(0,len(arr)-1):
    key = parse_line(arr[i])
    if is_valid_count(key[0], key[1], key[2], key[3]) == True:
        num_valid_count+=1
    elif is_valid_pos(key[0], key[1], key[2], key[3]) == True:
        num_valid_pos+=1

print("is_valid_count: " + str(num_valid_count))
print("is_valid_pos: " + str(num_valid_pos))
# Day 4: Passport Processing

from projects.helpers import io

rows = []



def add_to_rows(line):
    try:
        rows_item = line
        rows.append(rows_item)
    except ValueError:
        return

io.read_file_by_newline("day4.txt", add_to_rows)

#Function to create array of people from rows
def parse_people(rows):
    persons = []
    index = 0
    persons.append('')
    for row in rows:
        #print(row)
        if len(row) > 1:
            #print(index)
            row=row.rstrip()
            persons[index] = persons[index] + ' ' + row
        else:
            persons.append('')
            index += 1

    #for person in persons:
        #print(person)

    print("Number of peoeple in persons: ", len(persons))
    return persons

#Function for passport logic
def is_valid_passport_1(passport):
    req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    opt_fields = ["cid"]

    count = 0
    for field in req_fields:
        if field in passport:
            count += 1

    if count == len(req_fields):
        #call is_valid_passport_2?
        return 1
    else:
        return 0


persons = parse_people(rows)
num_valid_1 = 0
for person in persons:
    num_valid_1 += is_valid_passport_1(person)

print("Number of Valid Passports (logic - is_valid_passport_1): ", num_valid_1)




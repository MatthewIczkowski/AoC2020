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
            persons[index] = persons[index].strip()
        else:
            persons.append('')
            index += 1

    #for person in persons:
        #print(person)

    #print("Number of peoeple in persons: ", len(persons))
    return persons

#Function to create dictonary of attributes from person
def parse_person(person):
    attributes = dict(x.split(':') for x in person.split(' '))
    return attributes

#Function to test if passport has all the required fields
def is_valid_passport_1(passport):
    req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    opt_fields = ["cid"]

    count = 0
    for field in req_fields:
        if field in passport:
            count += 1

    if count == len(req_fields):
        return 1
    else:
        return 0

#Function to test if passport with all required fields meets the data validation criteria
def is_valid_passport_2(passport):

    hcl_chars = ['#', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    ecl_types = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    hair_color = passport['hcl']

    if len(passport['byr']) != 4 or int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        #print(passport, '\n', "Invalid passport, 'byr' out of range. 'byr': ", passport['byr'])
        return 0
    elif len(passport['iyr']) != 4 or int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        #print(passport, '\n', "Invalid passport, 'iyr' out of range. 'iyr': ", passport['iyr'])
        return 0
    elif len(passport['eyr']) != 4 or int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        #print(passport, '\n', "Invalid passport, 'eyr' out of range. 'eyr': ", passport['eyr'])
        return 0
    elif 'cm' not in passport['hgt'] and 'in' not in passport['hgt']:
        #print(passport, '\n', "Invalid passport, 'hgt' does not contain 'cm' or 'in'. 'hgt': ", passport['hgt'])
        return 0
    elif 'cm' in passport['hgt'] and (int(passport['hgt'].strip('cmin')) < 150 or int(passport['hgt'].strip('cmin')) > 193):
        #print(passport, '\n', "Invalid passport, 'hgt' out of cm range. 'hgt': ", passport['hgt'])
        return 0
    elif 'in' in passport['hgt'] and (int(passport['hgt'].strip('cmin')) < 59 or int(passport['hgt'].strip('cmin')) > 76):
        #print(passport, '\n', "Invalid passport, 'hgt' out of in range. 'hgt': ", passport['hgt'])
        return 0
    elif hair_color[0] != '#' or len(hair_color) != 7 or any(x not in hcl_chars for x in hair_color):
        #print(passport, '\n', "Invalid passport, 'hcl' does not match required format. 'hcl': ", hair_color)
        return 0
    elif passport['ecl'] not in ecl_types:
        # print(passport, '\n', "Invalid passport, 'ecl' does not match value in 'ecl' list. 'ecl': ", passport['ecl'])
        return 0
    elif len(passport['pid']) != 9 or not passport['pid'].isdigit():
        #print(passport, '\n', "Invalid passport, 'pid' does not match required format. 'pid': ", passport['pid'])
        return 0
    else:
        #print("Valid passport: ", '\n', passport)
        return 1

persons = parse_people(rows)
num_valid_1 = 0
num_valid_2 = 0
passdict = {}
for person in persons:
    if is_valid_passport_1(person) == 1:
        num_valid_1 += 1
        #If passport has all the required fields then see if passport has valid data
        passdict = parse_person(person)
        num_valid_2 += is_valid_passport_2(passdict)

print("Number of Valid Passports (logic - is_valid_passport_1): ", num_valid_1)
print("Number of Valid Passports (logic - is_valid_passport_2): ", num_valid_2)




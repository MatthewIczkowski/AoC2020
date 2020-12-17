# Day 6 : Custom Customs
from projects.helpers import io

dataset = []

def add_to_arr(line):
    try:
        dataset_item = line.strip('\n')
        dataset.append(dataset_item)
    except ValueError:
        return

io.read_file_by_newline("day6.txt", add_to_arr)

def parse_people(rows):
    persons = []
    index = 0
    persons.append('')
    for row in rows:
        #print(row)
        if len(row) >= 1:
            #print(index)
            row=row.rstrip()
            persons[index] = persons[index] + row
            persons[index] = persons[index].strip()
        else:
            persons.append('')
            index += 1

    #for person in persons:
        #print(person)

    #print("Number of peoeple in persons: ", len(persons))
    return persons

def find_unique(group):
    is_unique = []
    for letter in group:
        if letter not in is_unique:
            is_unique.append(letter)
    return len(is_unique)

forms = parse_people(dataset)
total = 0
for form in forms:
    total += find_unique(form)

print("total = ", total)
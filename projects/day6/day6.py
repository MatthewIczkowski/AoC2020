# Day 6 : Custom Customs
from projects.helpers import io
import string

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
            persons[index] = persons[index] + ' ' + row
            persons[index] = persons[index].strip()
        else:
            persons.append('')
            index += 1

    #for person in persons:
        #print(person)

    #print("Number of peoeple in persons: ", len(persons))
    return persons

def find_unique(group):
    group = group.replace(' ', '')
    is_unique = []
    for letter in group:
        if letter not in is_unique:
            is_unique.append(letter)
    return len(is_unique)

def find_common(group):
    people = 1
    for char in group:
        if char == ' ':
            people += 1
    groups = group.split()

    #create dictionary of lowercase alphabet
    alphabet = list(string.ascii_lowercase)
    alphabet_count = dict.fromkeys(alphabet, 0)

    count_common = 0
    if people == 1:
        return len(groups[0])
    else:
        for person in groups:
            for letter in person:
                alphabet_count[letter] += 1

        for value in alphabet_count.values():
            if value == people:
                count_common += 1
        return count_common

forms = parse_people(dataset)
total_unique = 0
total_common = 0
for form in forms:
    total_unique += find_unique(form)
    total_common += find_common(form)

print("total_unique = ", total_unique)
print("total_common = ", total_common)


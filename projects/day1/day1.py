# Day 1: Report Repair
from projects.helpers import io

A = []

def add_to_A(line):
    try:
        A_item = int(line)
        A.append(A_item)
    except ValueError:
        return


io.read_file_by_newline("day1.txt", add_to_A)

list_num = len(A)
num = 2020
x = 0
while x < list_num - 1:
    y = x + 1
    while y < list_num:
        if A[x] + A[y] == num:
            print(A[x], A[y], num, A[x] * A[y])
            break
        else:
            y += 1
    x += 1

x = 0
while x < list_num - 2:
    y = x + 1
    while y < list_num - 1:
        z = y + 1
        while z < list_num:
            if A[x] + A[y] + A[z] == num:
                print(A[x], A[y], A[z], num, A[x] * A[y] * A[z])
                break
            else:
                z += 1
        y += 1
    x += 1

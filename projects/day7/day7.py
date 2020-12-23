# Day 7 : Handy Haversacks
from projects.helpers import io
import string

dataset = []

def add_to_arr(line):
    try:
        dataset_item = line.strip('\n')
        dataset.append(dataset_item)
    except ValueError:
        return

io.read_file_by_newline("day7.txt", add_to_arr)

def find_outer(data):
    outer_bags = []
    for row in data:
        outer_bag, inner_bags = row.split("contain", 2)
        if "shiny gold bag" in inner_bags:
            outer_bag, scrap = outer_bag.split("bag", 2)
            outer_bags.append(outer_bag)
    return(outer_bags)


outer_gold = find_outer(dataset)
bag_count = 0
for bag in dataset:
    outer_bag, inner_bags = bag.split("contain", 2)
    if "shiny gold bag" in inner_bags or any(bag in inner_bags for bag in outer_gold):
        bag_count += 1
print("bag count: ", bag_count)



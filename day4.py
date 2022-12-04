import helper
import re

input_file = './inputs/day4'

def parse_pair(pair):
    elves = pair.split(',')
    elf_1 = elves[0].split('-')
    elf_2 = elves[1].split('-')
    return int(elf_1[0]), int(elf_1[1]), int(elf_2[0]), int(elf_2[1])

def part_1(pairs):
    contains_count = 0
    for pair in pairs:
        min_1, max_1, min_2, max_2 = parse_pair(pair)
        if (min_1 <= min_2 and max_1 >= max_2) or (min_2 <= min_1 and max_2 >= max_1):
            contains_count += 1
    return contains_count
    
def part_2(pairs):
    overlap_count = 0
    for pair in pairs:
        min_1, max_1, min_2, max_2 = parse_pair(pair)
        elf_1_range = range(min_1, max_1 + 1)
        elf_2_range = range(min_2, max_2 + 1)
        if min_1 in elf_2_range or max_1 in elf_2_range or min_2 in elf_1_range or max_2 in elf_1_range:
            overlap_count += 1
    return overlap_count

pairs = helper.read_file_as_list_of_strings(input_file)
print(part_1(pairs))
print(part_2(pairs))
import helper

input_file = './inputs/day3'

def priority(c):
    if c.isupper():
        return ord(c) - 38
    return ord(c) - 96
    
def get_common_item(rucksack):
    i = 0
    compartment_2 = set(rucksack[int(len(rucksack) / 2):])
    while i < len(rucksack) / 2:
        if rucksack[i] in compartment_2:
            return rucksack[i]
        i += 1
    return None
    
def part_1(rucksacks):
    priority_sum = 0
    for rucksack in rucksacks:
        common_item = get_common_item(rucksack)
        priority_sum += priority(common_item)
    return priority_sum
    
def get_common_item_in_group(rucksack_1, rucksack_2, rucksack_3):
    rucksack_2 = set(rucksack_2)
    rucksack_3 = set(rucksack_3)
    for item in rucksack_1:
        if item in rucksack_2 and item in rucksack_3:
            return item
    return None
    
def part_2(rucksacks):
    priority_sum = 0
    i = 0
    while i < len(rucksacks):
        rucksack_group = rucksacks[i:i+3]
        common_item = get_common_item_in_group(*rucksack_group)
        priority_sum += priority(common_item)
        i += 3
    return priority_sum
    
    
rucksacks = helper.read_file_as_list_of_strings(input_file)
print(part_1(rucksacks))
print(part_2(rucksacks))
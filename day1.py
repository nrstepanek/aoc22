import helper

input_file = './inputs/day1'

# Return the largest number of calories an elf has.
def part_1():
    lines = helper.read_file_as_list_of_strings(input_file)
    cur_calorie_total = 0
    cur_max_calorie_total = 0
    for line in lines:
        if not line:
            cur_max_calorie_total = max(cur_max_calorie_total, cur_calorie_total)
            cur_calorie_total = 0
        else:
            cur_calorie_total += int(line)
    return max(cur_max_calorie_total, cur_calorie_total)

# Return the total number of calories the top 3 elves have.
def part_2():
    lines = helper.read_file_as_list_of_strings(input_file)
    cur_calorie_total = 0
    top_3 = []
    for line in lines:
        if not line:
            top_3 = insert_sort(top_3, cur_calorie_total)[:3]
            cur_calorie_total = 0
        else:
            cur_calorie_total += int(line)
    return top_3

def insert_sort(list, to_insert):
    index = 0
    while index < len(list) and list[index] > to_insert:
        index += 1
    return list[:index] + [to_insert] + list[index:]

print(part_1())
print(sum(part_2()))
import helper
import re
 
input_file = './inputs/day5'
 
def parse_lines(lines):
    stack_lines = lines[:8]
    move_lines = lines[10:]
    stacks = [[] for _ in range(9)]
    
    for stack_line in stack_lines:
        i = 1
        si = 0
        while i < len(stack_line):
            if stack_line[i] != ' ':
                stacks[si].append(stack_line[i])
            si += 1
            i += 4
    
    for stack in stacks:
        stack.reverse()
    
    return stacks, move_lines
    
def parse_move_line(move_line):
    nums = re.findall(r'\d+', move_line)
    nums = [int(num) for num in nums]
    return tuple(nums)
    
def print_stacks(stacks):
    print('')
    for stack in stacks:
        print(stack)
    
def part_1(stacks, move_lines, reverse=True):
    for move_line in move_lines:
        print_stacks(stacks)
        print(move_line)
        num_to_move, start, end = parse_move_line(move_line)
        num_to_move = min(num_to_move, len(stacks[start-1]))
        to_move = stacks[start-1][-num_to_move:]
        if reverse:
            to_move.reverse()
        del stacks[start-1][-num_to_move:]
        stacks[end-1].extend(to_move)
    return stacks
 
def print_stack_tops(stacks):
    string = ''
    for stack in stacks:
        string += stack[-1]
    print(string)
 
lines = helper.read_file_as_list_of_strings(input_file)
stacks, move_lines = parse_lines(lines)
print_stack_tops(part_1(stacks, move_lines))
stacks, move_lines = parse_lines(lines)
print_stack_tops(part_1(stacks, move_lines, False))
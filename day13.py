import helper
from functools import cmp_to_key

input_file = './inputs/day13'

def compare_lists(l1, l2):
    i = 0
    while i < len(l1) or i < len(l2):
        if i >= len(l1):
            return True
        if i >= len(l2):
            return False
            
        if isinstance(l1[i], int) and isinstance(l2[i], int):
            if l1[i] < l2[i]:
                return True
            if l1[i] > l2[i]:
                return False
            i += 1
            continue
                
        if isinstance(l1[i], int):
            l1[i] = [l1[i]]
        if isinstance(l2[i], int):
            l2[i] = [l2[i]]
            
        result = compare_lists(l1[i], l2[i])
        if result is not None:
            return result
                
        i += 1
        
    return None

def compare(p1, p2):
    result = compare_lists(p1, p2)
    if result:
        return 1
    if result == None:
        return 0
    return -1
    
def print_lists(l):
    for list in l:
        print(list)
    
lines = helper.read_file_as_list_of_strings(input_file)
i = 0
index = 1
i_sum = 0
packet_list = []
while i < len(lines):
    p1 = eval(lines[i])
    p2 = eval(lines[i+1])
    packet_list.extend([p1, p2])
    result = compare_lists(p1, p2)
    print(result)
    if result:
        i_sum += index
    index += 1
    i += 3
print(i_sum)

print_lists(packet_list)
packet_list.extend([[[2]], [[6]]])
print('-------------------------------------------------')
packet_list = sorted(packet_list, key=cmp_to_key(compare), reverse=True)
print_lists(packet_list)
print((packet_list.index([[[[2]]]])+1) * (packet_list.index([[[[6]]]])+1))
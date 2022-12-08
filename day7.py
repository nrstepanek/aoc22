import helper
import itertools

input_file = './inputs/day7'

class Node:
    def __init__(self, is_dir, name):
        self.is_dir = is_dir
        self.name = name
        self.internal_nodes = {}
        
    def set_size(self, size):
        self.size = size
        
    def add_internal_node(self, node):
        self.internal_nodes[node.name] = node
        
    def get_internal_node(self, node_name):
        return self.internal_nodes[node_name]
        
    def total_size(self):
        size = 0
        for node in self.internal_nodes.values():
            if node.is_dir:
                size += node.total_size()
            else:
                size += node.size
        return size
        
    def __contains__(self, node_name):
        return node_name in self.internal_nodes.keys()
        
    def __str__(self):
        return self.name
        
    def pretty_print(self, depth):
        string = '/\n'
        for node in self.internal_nodes.values():
            if node.is_dir:
                string += (' ' * (depth*2+2)) + node.name + node.pretty_print(depth + 1)
            else:
                string += (' ' * (depth*2+2)) + node.name + ' ' + node.size + '\n'
        return string
        
                

def build_disk(command_output):
    top_level = Node(True, '/')
    cur_path = []
    cur_node = top_level
    for line in command_output:
        parts = line.split()
        if parts[0] == '$':
            if parts[1] == 'cd':
                if parts[2] == '/':
                    cur_node = top_level
                    cur_path = []
                elif parts[2] == '..':
                    cur_node = cur_path[-1]
                    del cur_path[-1]
                else:
                    cur_path.append(cur_node)
                    if parts[2] in cur_node:
                        cur_node = cur_node.get_internal_node(parts[2])
                    else:
                        new_node = Node(True, parts[2])
                        cur_node.add_internal_node(new_node)
                        cur_node = new_node
            elif parts[1] == 'ls':
                continue
        elif parts[0] == 'dir':
            if parts[1] not in cur_node:
                new_node = Node(True, parts[1])
                cur_node.add_internal_node(new_node)
        else:
            new_node = Node(False, parts[1])
            new_node.set_size(int(parts[0]))
            cur_node.add_internal_node(new_node)
            
    return top_level
    
def traverse_nodes(node):
    print(type(node))
    if node.is_dir:
        for internal_node in node.internal_nodes.values():
            traverse_nodes(internal_node)

def traverse_sizes(node):
    if node.is_dir:
        this_node_list = [node.total_size()]
        child_nodes_list = []
        for internal_node in node.internal_nodes.values():
            child_nodes_list.extend(traverse_sizes(internal_node))
        this_node_list.extend(child_nodes_list)
        return this_node_list
    return []

def part_1(disk):
    size_list = traverse_sizes(disk)
    total_size = 0
    for size in size_list:
        if size <= 100000:
            total_size += size
    return total_size
    
def part_2(disk):
    size_list = traverse_sizes(disk)
    space_available = 70000000 - size_list[0]
    need_to_free = 30000000 - space_available
    min_size = 9999999999
    for size in size_list:
        if size >= need_to_free:
            min_size = min(min_size, size)
    return min_size
    
command_output = helper.read_file_as_list_of_strings(input_file)
disk = build_disk(command_output)
print(part_1(disk))
print(part_2(disk))






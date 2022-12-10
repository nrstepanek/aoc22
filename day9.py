import helper
import math

input_file = './inputs/day9'

class Rope:

    dir_change_map = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
    
    def __init__(self, num_tails):
        self.head = (0, 0)
        self.tails = [(0, 0)] * num_tails
        self.tail_visited = set()
        self.tail_visited.add(self.tails[0])
        
    def move_head(self, dir):
        #print(dir)
        move_diff = self.dir_change_map[dir]
        self.head = (self.head[0] + move_diff[0], self.head[1] + move_diff[1])
        
        i = len(self.tails) - 1
        while i >= 0 and self.should_tail_move(i):
            self.move_tail(i)
            i -= 1
        #print(self.tail_visited)
        self.tail_visited.add(self.tails[0])
        
    def should_tail_move(self, tail_i):
        tail = self.tails[tail_i]
        if tail_i == len(self.tails) - 1:
            following = self.head
        else:
            following = self.tails[tail_i + 1]
        xd, yd = (following[0] - tail[0], following[1] - tail[1])
        return abs(xd) > 1 or abs(yd) > 1
        
    def move_tail(self, tail_i):
        tail = self.tails[tail_i]
        if tail_i == len(self.tails) - 1:
            following = self.head
        else:
            following = self.tails[tail_i + 1]
        xd, yd = (following[0] - tail[0], following[1] - tail[1])
        xd = math.ceil(xd / 2.0) if xd > 0 else math.floor(xd / 2.0)
        yd = math.ceil(yd / 2.0) if yd > 0 else math.floor(yd / 2.0)
        #print('Moving ' + str(tail_i) + ' to ' + str(tail[0] + xd) + ' ' + str(tail[1] + yd))
        self.tails[tail_i] = (tail[0] + xd, tail[1] + yd)
        

def parse_moves(moves):
    return [tuple(move.split(' ')) for move in moves]
    
def day_1(moves):
    rope = Rope(1)
    for move in moves:
        num_moves = int(move[1])
        while num_moves > 0:
            num_moves -= 1
            rope.move_head(move[0])
    return len(rope.tail_visited)
    
def day_2(moves):
    rope = Rope(9)
    for move in moves:
        num_moves = int(move[1])
        while num_moves > 0:
            num_moves -= 1
            rope.move_head(move[0])
    return len(rope.tail_visited)

moves = parse_moves(helper.read_file_as_list_of_strings(input_file))
print(day_1(moves))
print(day_2(moves))
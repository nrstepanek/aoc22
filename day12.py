import helper
import sys

input_file = './inputs/day12'

class HeightMap:
    def __init__(self, grid):
        self.grid = grid
        self.set_start_and_end()
        
    def set_start_and_end(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == 'S':
                    self.start = (r, c)
                elif self.grid[r][c] == 'E':
                    self.end = (r, c)
                    
    def get_a_cells(self):
        a_cells = []
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == 'a':
                    a_cells.append((r, c))
        return a_cells
                    
                    
    def get_possible_moves(self, r, c):
        potential_moves = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
        potential_moves = [move for move in potential_moves if move[0] >= 0 and move[1] >= 0 and move[0] < len(self.grid) and move[1] < len(self.grid[0])]
        possible_moves = [move for move in potential_moves if self.get_height(self.grid[move[0]][move[1]]) - self.get_height(self.grid[r][c]) <= 1]
        return possible_moves
        
    def get_height(self, c):
        if c == 'S':
            return ord('a')
        elif c == 'E':
            return ord('z')
        return ord(c)
        
    def bfs(self, start_cell=None):
        self.visited = set()
        if not start_cell:
            self.stack = [(self.start[0], self.start[1], 0)]
            self.visited.add(self.start)
        else:
            self.stack = [(start_cell[0], start_cell[1], 0)]
            self.visited.add(start_cell)
        
        done = False
        while not done and done is not None:
            #print(done)
            done = self.bfsr()
        return done
        
    def bfsr(self):
        #print(self.stack)
        #print(len(self.visited))
        if len(self.stack) == 0:
            return None
        (cur_r, cur_c, depth) = self.stack[0]
        if (cur_r, cur_c) == self.end:
            return depth
            
        for move in self.get_possible_moves(cur_r, cur_c):
            if move not in self.visited:
                self.stack.append((move[0], move[1], depth+1))
                self.visited.add((move[0], move[1]))
                
        del self.stack[0]
        return False
        
        
grid = helper.read_file_as_2d_list(input_file)
height_map = HeightMap(grid)
print(height_map.bfs())
a_cells = height_map.get_a_cells()
min_path = 2000
for a_cell in a_cells:
    length = height_map.bfs(a_cell)
    if length:
        min_path = min(min_path, length)
print(min_path)
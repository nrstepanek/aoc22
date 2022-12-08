import helper

input_file = './inputs/day8'
test_input_file = './inputs/day8test'

class TreeGrid:
    def __init__(self, grid):
        self.grid = grid
        self.visible_grid = [[0 for x in range(len(self.grid))] for y in range(len(self.grid[0]))]
        self.set_borders_visible()
        for row in range(len(self.grid)):
            self.set_visibility_for_row(row)
        for col in range(len(self.grid[0])):
            self.set_visibility_for_col(col)
        self.count_visible_trees()
        
    def set_borders_visible(self):
        for col in range(len(self.grid[0])):
            self.visible_grid[0][col] = 1
            self.visible_grid[-1][col] = 1
        for row in range(len(self.grid)):
            self.visible_grid[row][0] = 1
            self.visible_grid[row][-1] = 1
        
    def set_visibility_for_row(self, row):
        last_height = self.grid[row][0]
        col = 1
        while col < len(self.grid[row]):
            if self.grid[row][col] > last_height:
                self.visible_grid[row][col] = 1
                last_height = self.grid[row][col]
            col += 1
            
        last_height = self.grid[row][-1]
        col = len(self.grid[row]) - 2
        while col > 0:
            if self.grid[row][col] > last_height:
                self.visible_grid[row][col] = 1
                last_height = self.grid[row][col]
            col -= 1
        
    def set_visibility_for_col(self, col):
        last_height = self.grid[0][col]
        row = 1
        while row < len(self.grid):
            if self.grid[row][col] > last_height:
                self.visible_grid[row][col] = 1
                last_height = self.grid[row][col]
            row += 1
            
        last_height = self.grid[-1][col]
        row = len(self.grid) - 2
        while row > 0:
            if self.grid[row][col] > last_height:
                self.visible_grid[row][col] = 1
                last_height = self.grid[row][col]
            row -= 1
            
    def count_visible_trees(self):
        self.visible_count = 0
        for row in self.visible_grid:
            for visible in row:
                self.visible_count += visible
                
    def scenic_score(self, row, col):
        r = row
        c = col
        scores = [0, 0, 0, 0]
        middle_height = self.grid[row][col]
        
        r = row - 1
        done = False
        while r >= 0 and not done:
            if self.grid[r][c] >= middle_height:
                done = True
            scores[0] += 1
            r -= 1
            
        r = row + 1
        done = False
        while r < len(self.grid) and not done:
            if self.grid[r][c] >= middle_height:
                done = True
            scores[1] += 1
            r += 1
            
        r = row
        c = col - 1
        done = False
        while c >= 0 and not done:
            if self.grid[r][c] >= middle_height:
                done = True
            scores[2] += 1
            c -= 1
            
        c = col + 1
        done = False
        while c < len(self.grid[r]) and not done:
            if self.grid[r][c] >= middle_height:
                done = True
            scores[3] += 1
            c += 1
            
        return scores[0] * scores[1] * scores[2] * scores[3]
        
    def get_best_scenic_score(self):
        highest_score = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                highest_score = max(highest_score, self.scenic_score(row, col))
        return highest_score


grid = helper.read_file_as_2d_list_of_ints(input_file)
test_grid = helper.read_file_as_2d_list_of_ints(test_input_file)
tree_grid = TreeGrid(grid)
test_tree_grid = TreeGrid(test_grid)
print(tree_grid.visible_count)
print(tree_grid.get_best_scenic_score())
import helper

input_file = './inputs/day14'

def get_coords_between(start_coord, end_coord):
    dx = 0
    dy = 0
    if start_coord[0] < end_coord[0]:
        dx = 1
    elif start_coord[0] > end_coord[0]:
        dx = -1
    elif start_coord[1] < end_coord[1]:
        dy = 1
    elif start_coord[1] > end_coord[1]:
        dy = -1
    coords = [start_coord]
    while start_coord != end_coord:
        start_coord = (start_coord[0] + dx, start_coord[1] + dy)
        coords.append(start_coord)
    return coords

class CaveSystem:
    def __init__(self, rock_paths):
        self.grid = {}
        self.floor_y = -1
        for rock_path in rock_paths:
            rock_lines = rock_path.split(' -> ')
            rock_coords = [tuple(line.split(',')) for line in rock_lines]
            rock_coords = [(int(coord[0]), int(coord[1])) for coord in rock_coords]
            i = 0
            while i < len(rock_coords) - 1:
                start_coord = rock_coords[i]
                end_coord = rock_coords[i+1]
                coords_between = get_coords_between(start_coord, end_coord)
                for cb in coords_between:
                    self.grid[cb] = '#'
                    self.floor_y = max(self.floor_y, cb[1])
                i += 1
                
    def print_grid(self, start_x, end_x, start_y, end_y):
        for y in range(start_y, end_y):
            to_print = ''
            for x in range(start_x, end_x):
                if (x, y) in self.grid.keys():
                    to_print += self.grid[(x, y)]
                else:
                    to_print += '.'
            print(to_print)
            
    def add_sand(self, infinite_floor=False):
        self.sand_count = 0
        while self.add_sand_unit(infinite_floor):
            self.sand_count += 1
            
    def add_sand_unit(self, infinite_floor):
        sand_coord = (500, 0)
        if infinite_floor and (500, 0) in self.grid.keys():
            return False
        while True:
            if (sand_coord[0], sand_coord[1] + 1) not in self.grid.keys():
                sand_coord = (sand_coord[0], sand_coord[1] + 1)
            elif (sand_coord[0] - 1, sand_coord[1] + 1) not in self.grid.keys():
                sand_coord = (sand_coord[0] - 1, sand_coord[1] + 1)
            elif (sand_coord[0] + 1, sand_coord[1] + 1) not in self.grid.keys():
                sand_coord = (sand_coord[0] + 1, sand_coord[1] + 1)
            else:
                self.grid[sand_coord] = 'O'
                return True
            if not infinite_floor and sand_coord[1] > self.floor_y:
                return False
            if infinite_floor and sand_coord[1] == self.floor_y + 1:
                self.grid[sand_coord] = 'O'
                return True
            
                
            
        
        
rock_paths = helper.read_file_as_list_of_strings(input_file)
cave_system = CaveSystem(rock_paths)
cave_system.print_grid(494, 504, 0, 10)
cave_system.add_sand()
cave_system.print_grid(494, 504, 0, 10)
print(cave_system.sand_count)

cave_system = CaveSystem(rock_paths)
cave_system.print_grid(494, 504, 0, 10)
cave_system.add_sand(True)
cave_system.print_grid(494, 504, 0, 10)
print(cave_system.sand_count)
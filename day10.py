import helper

input_file = './inputs/day10'

class ComSystem():
    def __init__(self, instructions):
        self.instructions = instructions
        self.x = 1
        self.cycle_x = []
        self.read_instructions()
        self.screen = []
        
    def read_instructions(self):
        for instruction in self.instructions:
            self.cycle_x.append(self.x)
            if instruction[:4] == 'addx':
                self.cycle_x.append(self.x)
                self.x += int(instruction[5:])
                
    def pretty_print(self):
        to_print = ''
        for i in range(len(self.cycle_x)):
            to_print += str(i + 1) + ': ' + str(self.cycle_x[i]) + '\n'
        print(to_print)
                
    def signal_strength(self, cycle):
        return cycle * self.cycle_x[cycle - 1]
        
    def generate_screen(self):
        cycle = 1
        while cycle < 241:
            middle_x = (cycle-1) % 40
            if self.cycle_x[cycle - 1] in [middle_x - 1, middle_x, middle_x + 1]:
                self.screen.append('#')
            else:
                self.screen.append('.')
            cycle += 1
                
    def print_screen(self):
        i = 0
        to_print = ''
        while i < 6:
            to_print += ''.join(self.screen[i*40:(i+1)*40]) + '\n'
            i += 1
        print(to_print)
        

instructions = helper.read_file_as_list_of_strings(input_file)
com_system = ComSystem(instructions)

strength_sum = 0
for cycle in [20, 60, 100, 140, 180, 220]:
    strength_sum += com_system.signal_strength(cycle)
com_system.pretty_print()
print(strength_sum)
com_system.generate_screen()
com_system.print_screen()
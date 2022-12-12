import helper
import math

input_file = './inputs/day11'

class Monkey:
    def __init__(self, id, starting_items, throw_to_monkeys):
        self.id = id
        self.items = starting_items
        self.throw_to_monkeys = throw_to_monkeys
        self.inspect_count = 0
    
    def operation(self, level):
        if self.id == 0:
            return level * 11
        elif self.id == 1:
            return level + 8
        elif self.id == 2:
            return level * 3
        elif self.id == 3:
            return level + 4
        elif self.id == 4:
            return level * level
        elif self.id == 5:
            return level + 2
        elif self.id == 6:
            return level + 3
        elif self.id == 7:
            return level + 5
            
    def test(self, level):
        if self.id == 0:
            return level % 5 == 0
        elif self.id == 1:
            return level % 17 == 0
        elif self.id == 2:
            return level % 2 == 0
        elif self.id == 3:
            return level % 7 == 0
        elif self.id == 4:
            return level % 3 == 0
        elif self.id == 5:
            return level % 11 == 0
        elif self.id == 6:
            return level % 13 == 0
        elif self.id == 7:
            return level % 19 == 0
            
    def get_throw_to_monkey_id(self, test_result):
        if test_result:
            return self.throw_to_monkeys[0]
        return self.throw_to_monkeys[1]
        
class MonkeySimulator:
    def __init__(self, monkeys):
        self.monkeys = monkeys
        
    def turn(self, id):
        for item in self.monkeys[id].items:
            item = self.monkeys[id].operation(item)
            item = item % 9699690
            #item = math.floor(item / 3.0)
            throw_to_monkey_id = self.monkeys[id].get_throw_to_monkey_id(self.monkeys[id].test(item))
            self.monkeys[throw_to_monkey_id].items.append(item)
            self.monkeys[id].inspect_count += 1
        self.monkeys[id].items = []
        
    def round(self):
        for i in range(len(self.monkeys)):
            self.turn(i)
            
    def get_inspect_counts(self):
        return [m.inspect_count for m in self.monkeys]
        
        
monkeys = []
monkeys.append(Monkey(0, [77, 69, 76, 77, 50, 58], (1, 5)))
monkeys.append(Monkey(1, [75, 70, 82, 83, 96, 64, 62], (5, 6)))
monkeys.append(Monkey(2, [53], (0, 7)))
monkeys.append(Monkey(3, [85, 64, 93, 64, 99], (7, 2)))
monkeys.append(Monkey(4, [61, 92, 71], (2, 3)))
monkeys.append(Monkey(5, [79, 73, 50, 90], (4, 6)))
monkeys.append(Monkey(6, [50, 89], (4, 3)))
monkeys.append(Monkey(7, [83, 56, 64, 58, 93, 91, 56, 65], (1, 0)))

monkey_simulator = MonkeySimulator(monkeys)
for i in range(10000):
    print(monkey_simulator.get_inspect_counts())
    monkey_simulator.round()
print(monkey_simulator.get_inspect_counts())

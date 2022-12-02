import helper
 
input_file = './inputs/day2'
 
def is_rock(c):
    return c in ['A', 'X']
    
def is_paper(c):
    return c in ['B', 'Y']
    
def is_scissor(c):
    return c in ['C', 'Z']
    
def type_score(c):
    if is_rock(c):
        return 1
    if is_paper(c):
        return 2
    if is_scissor(c):
        return 3
    
def game_score(opponent, you):
    if is_rock(you):
        if is_rock(opponent):
            return 3
        if is_paper(opponent):
            return 0
        if is_scissor(opponent):
            return 6
    if is_paper(you):
        if is_rock(opponent):
            return 6
        if is_paper(opponent):
            return 3
        if is_scissor(opponent):
            return 0
    if is_scissor(you):
        if is_rock(opponent):
            return 0
        if is_paper(opponent):
            return 6
        if is_scissor(opponent):
            return 3
    return -99999999
    
def you_choose_score(opponent, outcome):
    if is_rock(opponent):
        if outcome == 'X':
            return 3
        if outcome == 'Y':
            return 1
        return 2
    if is_paper(opponent):
        if outcome == 'X':
            return 1
        if outcome == 'Y':
            return 2
        return 3
    if is_scissor(opponent):
        if outcome == 'X':
            return 2
        if outcome == 'Y':
            return 3
        return 1
            
def outcome_score(outcome):
    if outcome == 'X':
        return 0
    if outcome == 'Y':
        return 3
    return 6
    
def part_1():
    lines = helper.read_file_as_list_of_strings(input_file)
    score = 0
    for line in lines:
        opponent = line[0]
        you = line[2]
        score += game_score(opponent, you) + type_score(you)
    return score
    
def part_2():
    lines = helper.read_file_as_list_of_strings(input_file)
    score = 0
    for line in lines:
        opponent = line[0]
        outcome = line[2]
        score += you_choose_score(opponent, outcome) + outcome_score(outcome)
    return score
    
print(part_1())
print(part_2())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
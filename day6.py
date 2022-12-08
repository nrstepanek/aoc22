import helper

input_file = './inputs/day6'

def all_unique(string):
    return len(string) == len(set(string))

def find_first_unique(signal, num_chars):
    i = 0
    while i < len(signal) - num_chars:
        if all_unique(signal[i:i+num_chars]):
            return i + num_chars
        i += 1
    return -1


signal = helper.read_file_as_string(input_file)
print(find_first_unique(signal, 4))
print(find_first_unique(signal, 14))
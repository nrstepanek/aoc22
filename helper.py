
def read_file_as_string(filename):
    with open(filename) as file:
        return file.read()

def read_file_as_list_of_strings(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        return lines
        
def read_file_as_list_of_ints(filename):
    with open(filename) as file:
        lines = [int(line.rstrip()) for line in file]
        return lines
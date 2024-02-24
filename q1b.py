#1
def read_file_line_by_line(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            print(line, end='')
read_file_line_by_line('poem.txt')
#2
def count_non_t_lines(file_name):
    non_t_lines = 0
    with open(file_name, 'r') as file:
        for line in file:
            if not line.startswith('T'):
                non_t_lines += 1
    return non_t_lines
non_t_lines = count_non_t_lines('story.txt')
print(f'Number of lines that do not start with "T": {non_t_lines}')
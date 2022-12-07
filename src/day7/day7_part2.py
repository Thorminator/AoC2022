import re

from src.day7.directory import Directory
from src.day7.file import File


def change_directory(arg, current_dir):
    if arg == '/':
        return root
    elif arg == '..':
        return current_dir.get_containing_dir()
    else:
        new_dir = Directory(arg, current_dir)
        return current_dir.add_file(new_dir)


def get_command_match(line):
    return re.match(r'\$ (?P<command>\w+)\s?(?P<arg>.*)', line.strip())


def get_next_command_index(lines, index):
    next_index = index + 1
    while next_index < len(lines) and not (get_command_match(lines[next_index])):
        next_index += 1
    return next_index


def parse_ls_lines(lines, index, current_dir):
    next_command_index = get_next_command_index(lines, index)
    ls_lines = [s.strip() for s in lines[index + 1:next_command_index]]
    for line in ls_lines:
        match = re.match(r'(.+?)\s(.+)', line)
        if match.group(1) == 'dir':
            current_dir.add_file(Directory(match.group(2), current_dir))
        else:
            current_dir.add_file(File(match.group(2), int(match.group(1))))
    return next_command_index - 1


def find_directories_of_size_in(directory):
    res = []
    for file in directory.files:
        if isinstance(file, Directory):
            if file.get_size() >= 4359867:
                res.append(file)
            res = res + find_directories_of_size_in(file)
    return res


if __name__ == '__main__':
    root = Directory('/', None)
    current_dir = root
    
    lines = open('input.txt', 'r').readlines()
    
    for index in range(len(lines)):
        line = lines[index]
        match = get_command_match(line)
        if match:
            group_dict = match.groupdict()
            command = group_dict.get('command')
            arg = group_dict.get('arg')
            if command == 'cd':
                current_dir = change_directory(arg, current_dir)
            elif command == 'ls':
                index = parse_ls_lines(lines, index, current_dir)
        index += 1

    files = [f for f in find_directories_of_size_in(root)]
    print(min([f.get_size() for f in files]))

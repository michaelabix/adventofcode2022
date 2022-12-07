def read_file(file_path: str) -> list:
    """this is really gross"""
    file_object = open(file_path, "r", encoding="UTF=8").read().splitlines()
    directory_structure = {}
    path = ''
    length = len(file_object)
    i = 0
    while i < length:
        line = file_object[i].split()
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '..':
                    index = path.rfind("/")
                    path = path[:index]
                    if path == '':
                        path = '/'
                else:
                    if line[2] == '/':
                        path = '/'
                    else:
                        if path == '/':
                            path += (line[2])
                        else:
                            path += ('/' + line[2])
                    directory_structure[path] = []
        else:
            if line[0] == 'dir':
                if line[1] != '/':
                    tmp = line[1]
                    if path == '/':
                        line[1] = path + tmp
                    else:
                        line[1] = path + '/' + tmp
                    directory_structure[path].append(tuple(line))
            else:
                directory_structure[path].append(tuple(line))
        i += 1
    
    return directory_structure


def total_size(directory_structure: list, size: int):
    dir_size = {}
    for d in directory_structure:
        dir_size[d] = calculate(d, directory_structure)
    sizes = list(dir_size.values())
    sum = 0
    for s in sizes:
        if int(s) < size:
            sum += s
    return sum, dir_size


def calculate(dir: tuple, directory_structures: list) -> int:
    size = 0
    for item in directory_structures[dir]:
        if item[0] != 'dir':
            size += int(item[0])
        else:
            size += calculate(item[1], directory_structures)
    return size


def delete(total_space: int, min_space: int, dir_size: dict) -> int:
    used_space = dir_size['/']
    delete = min_space - (total_space - used_space)
    values = list(dir_size.values())
    values.sort()
    for v in values:
        if v > delete:
            return v
    return 0


def main():
    directory_structure = read_file("puzzle_input.txt")
    total, dir_size = total_size(directory_structure, 100000)
    print('the answer to part 1 is ' + str(total))
    deleted = delete(70000000, 30000000, dir_size)
    print('the answer to part 2 is ' + str(deleted))


if __name__ == "__main__":
    main()



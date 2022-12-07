import re
import copy

def read_file(file_path: str) -> list:
    """lazy parsing"""
    file_object = open(file_path, "r", encoding="UTF=8").read().splitlines()
    instructions = []
    for l in file_object:
        if l.startswith(' 1'):
            array_size = [int(i) for i in re.findall(r'\d+', l)]
        if l.startswith('move'):
            tmp = [int(i) for i in re.findall(r'\d+', l)]
            instructions.append(tmp)
    containers = [[] for x in range(len(array_size))]
    for l in file_object:
        if '[' in l:
            tmp = []
            for i, c in enumerate(l):
                if (i + 1 & 3) != 0:
                    tmp.append(c)
            tmp2 = ''.join(tmp)

            tmp3 = re.findall('...', tmp2)
            for i, t in enumerate(tmp3):
                if t != '   ':
                    pattern = re.compile('[\W_]+')
                    tmp3[i] = pattern.sub('', t)
                    containers[i].insert(0, tmp3[i])
                
    return containers, instructions


def move(containers: list, instructions: list, crane_mover=9000) -> str:
    """handles crane instructions for moving crates"""
    for i in instructions:
        num, from_stack, to_stack = i
        if crane_mover == 9001:
            tmp = containers[from_stack - 1][-num:]
            containers[from_stack - 1] = containers[from_stack - 1][:-num]
            containers[to_stack - 1].extend(tmp)
        else:
            for x in range(num):
                containers[to_stack - 1].append(containers[from_stack - 1].pop())
        
    top = [x[-1] for x in containers]
    return ''.join(top)


def main():
    containers, instructions = read_file("puzzle_input.txt")
    print("the answer to part 1 is " + move(copy.deepcopy(containers), instructions))
    print("the answer to part 2 is " + move(copy.deepcopy(containers), instructions, 9001))


if __name__ == "__main__":
    main()
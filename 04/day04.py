def read_file(file_path: str) -> list:
    """lazy parsing"""
    file_object = open(file_path, "r", encoding="UTF=8").read().splitlines()
    sections = []
    for f in file_object:
        tmp = f.split(',')
        temp = []
        for t in tmp:
            ts = t.split('-')
            temp.append((int(ts[0]), int(ts[1])))
        sections.append(temp)
    return sections


def find_complete_overlap(sections: list) -> int:
    count = 0
    for s in sections:
        if s[0][0] <= s[1][0] and s[0][1] >= s[1][1]:
            count += 1
        elif s[1][0] <= s[0][0] and s[1][1] >= s[0][1]:
            count += 1

    return count


def find_some_overlap(sections: list) -> int:
    count = 0
    for s in sections:
        if s[0][1] >= s[1][0] and not s[0][0] > s[1][1] :
            count += 1

    return count


def main():
    sections = read_file("puzzle_input.txt")
    print("The answer to part 1 is " + str(find_complete_overlap(sections)))
    print("The answer to part two is " + str(find_some_overlap(sections)))
    
if __name__ == "__main__":
    main()
def read_file(file_path: str) -> list:
    """lazy parsing"""
    file_object = open(file_path, "r", encoding="UTF=8").read().splitlines()
    return file_object


def find_position(buffer: str, size: int) -> int:
    index = 0
    for i, c in enumerate(buffer):
        substring = buffer[i:i+size]
        if not checkChars(substring):
            index = i + size
            break
    return index


def checkChars(s: str) -> bool:
    for c in s:
        if s.count(c) > 1:
            return True
    return False


def main():
    buffer = read_file("puzzle_input.txt")[0]
    print("the answer to part 1 is " + str(find_position(buffer, 4)))
    print("the answer to part 2 is " + str(find_position(buffer, 14)))
    
if __name__ == "__main__":
    main()
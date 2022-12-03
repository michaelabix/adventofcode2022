import string


def read_file(file_path: str) -> list:
    """lazy parsing"""
    file_object = open(file_path, "r", encoding="UTF=8").read().splitlines()
    return file_object


def find_duplicates(in_rucksack: list) -> list:
    """find duplicate letters in two halves of string"""
    duplicates = []
    for i in in_rucksack:
        strings = [i[:len(i)//2], i[len(i)//2:]]
        common = set.intersection(*map(set, strings))
        if len(common) == 1:
            duplicates.append(list(common)[0])
        else:
            print("Something went wrong, too many or too few duplicate characters")
    return duplicates


def calculate(duplicates: list) -> int:
    """find score based on alphabet position a-zA-Z"""
    alphabet = string.ascii_letters
    score = 0
    for d in duplicates:
        score += (alphabet.find(d) + 1)
    return score


def split_rucksack(in_rucksack: list, n: int) -> list:
    """split items in rucksack into every three"""
    return list(zip(*[iter(in_rucksack)]*n))


def find_badge(in_rucksack_split: list) -> list:
    """find the badge in sets of three items"""
    badges = []
    for i in in_rucksack_split:
        common = set.intersection(*map(set, i))
        if len(common) == 1:
            badges.append(list(common)[0])
        else:
            print("Something went wrong, too many or too few badges")
    return badges


def main():
    in_rucksack = read_file("puzzle_input.txt")
    duplicates = find_duplicates(in_rucksack)
    print("The score for part 1 is " + str(calculate(duplicates)))
    in_rucksack_thirds = split_rucksack(in_rucksack, 3)
    badges = find_badge(in_rucksack_thirds)
    print("The score for part 2 is " + str(calculate(badges)))

    
if __name__ == "__main__":
    main()
def read_file(file_path: str) -> list:
    """lazy parsing"""
    calories = []
    file_object = open(file_path, "r", encoding="UTF=8").read().splitlines()
    for f in file_object:
        if not f:
            calories.append(0)
        else:
            calories.append(int(f))
    return calories


def find_totals(calories: list) -> int:
    """find total calories per elf"""
    totals = []
    temp_int = 0

    #do some math and append
    for c in calories:
        if c != 0:
            temp_int += c
        else:
            totals.append(temp_int)
            temp_int = 0

    #for the last set of calories
    totals.append(temp_int)

    #sort highest to lowest
    totals.sort(reverse=True)

    return totals


def top_three(calories: list) -> int:
    """find the total of the top three"""
    total = 0
    for i in range(0, 3):
        total += calories[i]

    return total


def main():
    calories = read_file("puzzle_input.txt")
    totals = find_totals(calories)

    #answers
    print("\nPart 1:")
    print("The highest set of calories totals " + str(totals[0]) + "\n")
    print("Part 2:")
    print("The top three elves are carrying " + str(top_three(totals)) + " calories \n")


if __name__ == "__main__":
    main()
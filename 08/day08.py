def read_file(file_path: str) -> list:
    """lazy parsing"""
    trees = []
    file_object = open(file_path, "r", encoding="UTF=8").read().splitlines()
    for f in file_object:
        int_list = [int(x) for x in f]
        trees.append(int_list)
    return trees


def tree_cover(trees: list) -> int:
    """find tree cover"""
    cover = []
    total = 0
    for t in trees:
        cover.append([0 * i for i in range(len(t))])
    i = 0
    length = len(trees[0])
    height = len(trees)
    while i < height:
        j = 0
        while j < length:
            if (i == 0 or i == height - 1):
                cover[i][j] = 1
                next
            elif (j == 0 or j == length - 1):
                cover[i][j] = 1
                next
            else:
                if check_row(trees, i, j) or check_column(trees, i, j):
                    cover[i][j] = 1
            j += 1
        i += 1
    for c in cover:
        total += c.count(1)
    return total


def check_row(trees: list, i: int, j: int) -> bool:
    cover_left = 0
    cover_right = 0
    cover = 0
    x = 0
    y = len(trees[0]) - 1
    while x < j:
        if trees[i][j] > trees[i][x]:
            cover_left = 1
        else:
            cover_left = 0
            break
        x += 1
    
    while y > j:
        if trees[i][j] > trees[i][y]:
            cover_right = 1
        else:
            cover_right = 0
            break
        y -= 1

    if cover_left or cover_right:
        cover = 1

    return cover


def check_column(trees: list, i: int, j: int) -> bool:
    cover_up = 0
    cover_down = 0
    cover = 0

    x = 0
    y = len(trees) - 1
    while x < i:
        if trees[i][j] > trees[x][j]:
            cover_up = 1
        else:
            cover_up = 0
            break
        x += 1
    
    while y > i:
        if trees[i][j] > trees[y][j]:
            cover_down = 1
        else:
            cover_down = 0
            break
        y -= 1

    if cover_up or cover_down:
        cover = 1

    return cover


def scenic_score(trees: list) -> int:
    """find spot for treehouse by measuring best scenery"""
    scenic = []
    for t in trees:
        scenic.append([0 * i for i in range(len(t))])
    x = 1
    height = (len(trees[1:-1]))
    width = len(trees[0][1:-1])
    while x <= width:
        y = 1
        while y <= height:
            scenic[x][y] = score(x, y, trees)
            y += 1
        x += 1
    largest = []
    for s in scenic:
        s.sort()
        largest.append(s[-1])
    largest.sort()
    return largest[-1]


def score(x, y, trees):
    """this is gross"""
    d = {'up': 0, 'down': 0, 'left': 0, 'right':0}
    min = 0
    max = len(trees) - 1
    for direction in d:
        stop = 0
        if direction == 'up':
            index = x
            while index > min and stop == 0:
                d[direction] += 1
                index = index - 1
                if trees[index][y] >= trees[x][y]:
                    stop = 1
        elif direction == 'down':
            index = x
            while index < max and stop == 0:
                d[direction] += 1
                index = index + 1
                if trees[index][y] >= trees[x][y]:
                    stop = 1
        elif direction == 'left':
            index = y
            while index > min and stop == 0:
                d[direction] += 1
                index = index - 1
                if trees[x][index] >= trees[x][y]:
                    stop = 1
        elif direction == 'right':
            index = y
            while index < max and stop == 0:
                d[direction] += 1
                index = index + 1
                if trees[x][index] >= trees[x][y]:
                    stop = 1
    score = d['up'] * d['down'] * d['left'] * d['right']
    return score


def main():
    trees = read_file("puzzle_input.txt")
    print("the answer to part 1 is " + str(tree_cover(trees)) )
    print("the answer to part 2 is " + str(scenic_score(trees)))
if __name__ == "__main__":
    main()
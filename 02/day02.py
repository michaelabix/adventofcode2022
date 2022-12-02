CONST_SCORES = {"X": 1, "Y": 2, "Z": 3, "W": 6, "L": 0, "D": 3}
CONST_ACTION = {"A": "rock", "B": "paper", "C": "scissors", "X": "rock", "Y": "paper", "Z": "scissors"}
CONST_SCORES2 = {"A": 1, "B": 2, "C": 3, "W": 6, "L": 0, "D": 3}
CONST_ACTION2 = {"A": "rock", "B": "paper", "C": "scissors", "X": "L", "Y": "D", "Z": "W"}


def read_file(file_path: str) -> list:
    """lazy parsing"""
    game_outcomes = []
    file_object = open(file_path, "r", encoding="UTF=8").read().splitlines()
    for f in file_object:
        game_outcomes.append(tuple(f.split()))
    return game_outcomes


def find_winner(game: tuple) -> str:
    """Find winner for part 1"""
    opponent = game[0]
    player = game[1]
    if CONST_ACTION[opponent] == CONST_ACTION[player]:
        return "D"
    elif CONST_ACTION[opponent] == 'rock':
        if CONST_ACTION[player] == 'paper':
            return "W"
        else:
            return "L"
    elif CONST_ACTION[opponent] == 'paper':
        if CONST_ACTION[player] == 'scissors':
            return "W"
        else:
            return "L"
    elif CONST_ACTION[opponent] == 'scissors':
        if CONST_ACTION[player] == 'rock':
            return "W"
        else:
            return "L"
    else:
        return "L"


def find_move(game: tuple) -> tuple:
    """interpret move and game outcome for part 2"""
    opponent = game[0]
    outcome = CONST_ACTION2[game[1]]
    move = game[0]
    if outcome == 'D':
        return move, outcome

    if CONST_ACTION2[opponent] == 'rock':
        if outcome == 'W':
            move = 'B'
        else:
            move = 'C'
    elif CONST_ACTION2[opponent] == 'paper':
        if outcome == 'W':
            move = 'C'
        else:
            move = 'A'
    elif CONST_ACTION2[opponent] == 'scissors':
        if outcome == 'W':
            move = 'A'
        else:
            move = 'B'
    
    return move, outcome


def score(game_outcomes: list, play_for = False) -> int:
    """find scores for part 1 and part 2"""
    total_score = 0
    if not play_for:
        for g in game_outcomes:
            total_score += CONST_SCORES[g[1]]
            total_score += CONST_SCORES[find_winner(g)]
    else:
        for g in game_outcomes:
            move = find_move(g)
            total_score += CONST_SCORES2[move[0]]
            total_score += CONST_SCORES2[move[1]]

    return total_score


def main():
    game_outcomes = read_file("puzzle_input.txt")
    print("The total score for Part 1 is " + str(score(game_outcomes)))
    print("The total score for part 2 is " + str(score(game_outcomes, True)))


if __name__ == "__main__":
    main()
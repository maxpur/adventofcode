# determine solution for star one of task two
def calc_game_part_one(file):
    sum = 0
    for line in file:
        args = line.split()
        sum += calc_points(args[0], args[1])
    return sum


# determine solution for star two of task two
def calc_game_part_two(file):
    sum = 0
    for line in file:
        args = line.split()
        sum += calc_points(args[0], determine_next_move(args[0], args[1]))
    return sum


# calc all points per round
def calc_points(input_A, input_B):
    points_per_sign = calc_points_per_sign(input_B)
    points_per_round = calc_points_per_round(input_A, input_B)
    return sum((points_per_round, points_per_sign))


# calc points depending on move
def calc_points_per_sign(sign):
    match sign:
        case 'X':
            return 1 
        case 'Y':
            return 2
        case 'Z':
            return 3
        case _:
            return 0


# calc points depending on game outcome
def calc_points_per_round(input_A, input_B):
    if is_lose(input_A, input_B):
        return 0
    elif is_draw(input_A, input_B): 
        return 3
    else: 
        return 6


# check if player B loses
def is_lose(input_A, input_B):
    return (input_A == 'A' and input_B == 'Z') or (input_A == 'B' and input_B == 'X') or (input_A == 'C' and input_B == 'Y')


# check if input results in a draw
def is_draw(input_A, input_B):
    return (input_A == 'A' and input_B == 'X') or (input_A == 'B' and input_B == 'Y') or (input_A == 'C' and input_B == 'Z')


# determine next move according to game outcome and input of player A
def determine_next_move(input_A, input_B):
    if input_B == "X":
        if input_A == "A":
            return "Z"
        elif input_A == "B":
            return "X"
        elif input_A == "C":
            return "Y"
    elif input_B == "Y":
        if input_A == "A":
            return "X"
        elif input_A == "B":
            return "Y"
        elif input_A == "C":
            return "Z"
    elif input_B == "Z": 
        if input_A == "A":
            return "Y"
        elif input_A == "B":
            return "Z"
        elif input_A == "C": 
            return "X"


def main():
    file = open("task2.txt", "r")
    print(f'Points part one: {calc_game_part_one(file)}')
    # re-read file
    file = open("task2.txt", "r")
    print(f'Points part two: {calc_game_part_two(file)}')


if __name__ == "__main__":
    main()
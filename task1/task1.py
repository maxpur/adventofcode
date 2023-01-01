# Determine sum of calories with maximum comparison
def get_max_calories(file):
    maximum = -1
    calories = 0
    for line in file:
        if line != "\n":
            calories = calories + int(line.rstrip("\n"))
        else:
            maximum = max(maximum, calories)
            calories = 0 
    return maximum


# Determine three highest calories
def get_first_three_max_calories(file):
    maximum1, maximum2, maximum3 = -1, -1, -1
    calories = 0
    for line in file:
        if line != "\n":
            calories = calories + int(line.rstrip("\n"))
        else:
            # in general update each time when calories is higher than current maxima
            # each time a maximum is updated values from higher maxima are shifted downwards
            if calories > maximum1:
                maximum3 = maximum2
                maximum2 = maximum1
                maximum1 = calories
            elif calories < maximum1 and calories > maximum2:
                maximum3 = maximum2
                maximum2 = calories
            elif calories < maximum2 and calories > maximum3:
                maximum3 = calories
            calories = 0
    return (maximum1, maximum2, maximum3)


def main():
    file = open("task1.txt", "r")
    print(f'Max calories: {sum(get_first_three_max_calories(file))}')

    
if __name__ == "__main__":
    main()
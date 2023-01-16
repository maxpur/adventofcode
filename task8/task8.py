# Parse file into multi-dimensional list
def pre_process_file(file):
    data = list()
    for line in file:
        line = line.rsplit("\n")[0]
        data.append(list(map(int, line)))
    return data


# Calculate all visible trees as required in task
def count_visible_trees(file):
    grid = pre_process_file(file)
    return count_edge_trees(grid) + count_interior_trees(grid)


# Count trees at the edge of the grid
def count_edge_trees(data):
    return 2 * len(data) + len(data[0]) + len(data[len(data) - 1]) - 4


# Count trees in between the the edges of the grid
def count_interior_trees(data):
    counter = 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) - 1):
            if is_horizontal_visible(data, i, j) or is_vertical_visible(data, i, j):
                counter += 1
    return counter


# Check if tree is visible in horizontal orientation
def is_horizontal_visible(data, row, column):
    height = data[row][column]
    visible_left = True
    for i in range(0, column):
        visible_left = visible_left and data[row][i] < height
    visible_right = True
    for i in range(column + 1, len(data[i])):
        visible_right = visible_right and data[row][i] < height
    return visible_left or visible_right


# Check if tree is visible in vertical orientation
def is_vertical_visible(data, row, column):
    height = data[row][column]
    visible_up = True
    for i in range(0, row):
        visible_up = visible_up and data[i][column] < height
    visible_down = True
    for i in range(row + 1, len(data)):
        visible_down = visible_down and data[i][column] < height
    return visible_up or visible_down


# Calculate max scenic score as defined in task
def compute_scenic_score(file):
    data = pre_process_file(file)
    maximum = 0
    for row in range( 1, len(data) - 1):
        for column in range(1, len(data[row]) - 1):
            score = compute_vertical_distance(data, row, column) * compute_horizontal_distance(data, row, column)
            maximum = max(score, maximum)
    return maximum


# Calculate vertical scenic of grid
def compute_vertical_distance(data, row, column):
    distance_up = 0
    distance_down = 0
    height = data[row][column]

    for i in range(row - 1, -1, -1):
        if data[i][column] < height:
            distance_up += 1
        elif data[i][column] >= height:
            distance_up += 1
            break 
    for i in range(row + 1, len(data)):
        if data[i][column] < height:
            distance_down += 1
        elif data[i][column] >= height:
            distance_down += 1
            break 
    return distance_up * distance_down


# Calculate horizontal scenic of grid
def compute_horizontal_distance(data, row, column):
    distance_left = 0
    distance_right = 0
    height = data[row][column]
    for i in range(column - 1, -1, -1):
        if data[row][i] < height:
            distance_left += 1
        elif data[row][i] >= height:
            distance_left += 1
            break 
    for i in range(column + 1, len(data[row])):
        if data[row][i] < height:
            distance_right += 1
        elif data[row][i] >= height:
            distance_right += 1
            break 
    return distance_left * distance_right


def main():
    file = open("task8.txt", "r")
    print(f'Solution star one: {count_visible_trees(file)}')
    file = open("task8.txt", "r")
    print(f'Solution star two: {compute_scenic_score(file)}')


if __name__ == "__main__":
    main()
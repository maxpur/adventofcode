# initialize crane as defined in task five
def init():
    crane1 = ['H','C','R']
    crane2 = ['B','J','H','L','S','F']
    crane3 = ['R','M','D','H','J','T','Q']
    crane4 = ['S','G','R','H','Z','B','J']
    crane5 = ['R','P','F','Z','T','D','C','B']
    crane6 = ['T','H','C','G']
    crane7 = ['S','N','V','Z','B','P','W','L']
    crane8 = ['R','J','Q','G','C']
    crane9 = ['L','D','T','R','H','P','F','S']
    return [crane1, crane2, crane3, crane4, crane5, crane6, crane7, crane8, crane9]


# parse command to process number of crates which need to be moved
def parse_command(line):
    line = line.rsplit("\n")[0]
    cmd = line.split()
    return (cmd[1],cmd[3],cmd[5])


# move crates from one stack to another stack
def execute_command_crate_mover_9000(cmd, crates):
    for i in range(0, int(cmd[0])):
        crates[int(cmd[2]) - 1].append(crates[int(cmd[1]) - 1].pop())
    return crates


# determine the highest crane of each stack
def get_highest_crates(crates):
    solution = ""
    for crane in crates:
        solution += crane.pop()
    return solution


# move each single crate from one stack to another
def move_single_crates(file):
    crates = init()
    for line in file:
        crates = execute_command_crate_mover_9000(parse_command(line), crates)
    return get_highest_crates(crates)


# execute commands as they are defined for move_crater 9001 which means
# that a sequence of crates can be moved without changing order
def execute_command_crate_mover_9001(cmd, crates):
    position = len(crates[int(cmd[2]) - 1])
    for i in range(0,int(cmd[0])):
        crates[int(cmd[2]) - 1].insert(position, crates[int(cmd[1]) - 1].pop())
    return crates


# move multiple crates without change in order
def move_multiple_crates(file):
    crates = init()
    for line in file:
        crates = execute_command_crate_mover_9001(parse_command(line), crates)
    return get_highest_crates(crates)


def main():
    file = open("task5.txt", "r")
    print(f'Highest crates star one: {move_single_crates(file)}')
    file = open("task5.txt", "r")
    print(f'Highest crates star two: {move_multiple_crates(file)}')


if __name__ == "__main__":
    main()
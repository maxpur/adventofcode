class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def to_string(self, num) -> str:
        return '\t' * num + f'- {self.name} (file, size={self.size})\n'

    def get_size(self):
        return self.size


class Directory:
    def __init__(self, name, parent = None) -> None:
        self.name = name
        self.parent = parent
        self.directories = list()
        self.files = list()

    def add_file(self, file):
        for el in self.files:
            if el.name == file.name:
                return False
        self.files.append(file)
        return True

    def add_directory(self, directory):
        for dir in self.directories:
            if dir.name == directory.name:
                return False
        self.directories.append(directory)
        return True

    def to_string(self, num):
        string = '\t' * num + f'- {self.name} (dir)\n'
        for dir in self.directories:
            string += f'\t{dir.to_string(num + 1)}'
        for file in self.files:
            string += f'\t{file.to_string(num +  1)}'
        return string

    def get_size(self):
        size = 0
        for file in self.files:
            size += file.get_size()
        for directory in self.directories:
            size += directory.get_size()
        return size


def get_command(line):
    line = line.split()
    if line[1] == 'ls':
        return (0, '')
    else:
        return (1, line[2])


def get_content(line):
    line = line.split()
    return (line[0],line[1])


def print_tree(dir):
    print(dir.to_string(0))


def process_tree(file):
    current, home = None, None
    for line in file:
        line = line.rsplit('\n')[0]
        if '$' in line:
            cmd = get_command(line)
            if cmd[0] == 0:
                # just read next lines
                continue
            elif cmd[0] == 1 and cmd[1] == '..':
                current = current.parent
            elif cmd[0] == 1:
                if home == None:
                    home = Directory(cmd[1])
                    current = home
                else:
                    for dir in current.directories:
                        if dir.name == cmd[1]:
                            current = dir       
        else:
            content = get_content(line)
            if content[0] == 'dir':
                current.add_directory(Directory(content[1], current))
            else:
                current.add_file(File(content[1], content[0]))
    return home


def count_bytes(file):
    tree = process_tree(file)
    size = 0
    print(tree.to_string(0))
    # TODO: implement counting of bytes for separat folders
    return size


def main():
    file = open('task7.txt', 'r')
    count_bytes(file)


if __name__ == '__main__':
    main()
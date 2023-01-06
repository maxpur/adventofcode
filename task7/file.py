class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size 
    
    def to_string(self):
        return f'{self.name} (file, size={self.size})'
    

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = list()
        self.directories = list()

    def add_directory(self, dir):
        self.directories.append(dir)

    def contains_directory(self, dir_name):
        for directory in self.directories:
            if directory.name == dir_name:
                return True
        return False

    def contains_file(self, file_name):
        for file in self.files:
            if file.name == file_name:
                return True
        return False
            
    def add_file(self, file):
        self.files.append(file)

    def get_size(self):
        size = 0
        for file in self.files:
            size += file.size
        for directory in self.directories:
            size += directory.get_size()
        return size

    def to_string(self):
        tree = ''
        tree += '-' + self.name + (' dir') + '\n'
        for dir in self.directories:
            tree += ' ' + dir.to_string()
        for file in self.files:
            tree += ' -' + file.to_string() + '\n'
   
        return tree
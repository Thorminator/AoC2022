class Directory:
    def __init__(self, name, containing_dir):
        self.name = name
        self.containing_dir = containing_dir
        self.files = []
    
    def get_size(self):
        return sum([f.get_size() for f in self.files])
    
    def get_containing_dir(self):
        return self.containing_dir
    
    def add_file(self, file):
        matched_files = [f for f in self.files if f.name == file.name]
        if len(matched_files) > 0:
            return matched_files[0]
        else:
            self.files.append(file)
            return file
    
    def print(self, prefix=''):
        print(f'{prefix}- {self.name} (dir)')
        for file in self.files:
            file.print(prefix + '  ')

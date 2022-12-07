class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def get_size(self):
        return self.size
    
    def print(self, prefix):
        print(f'{prefix}- {self.name} (file, size={self.size})')

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
    
    def get_size(self):
        return sum([f.get_size() for f in self.files])


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def get_size(self):
        return self.size


root = Directory('/')
for line in open('text.txt', 'r').readlines():


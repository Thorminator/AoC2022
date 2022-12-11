class Monkey:
    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test
        self.inspected = 0
        
    def inspect_all_items(self):
        self.inspected += len(self.items)
        items = [item for item in self.items]
        self.items.clear()
        return items

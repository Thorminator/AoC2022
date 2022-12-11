import re


class TestPredicate:
    def __init__(self, test, operand, monkey_true, monkey_false):
        self.test = test
        self.operand = operand
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false
    
    def monkey_from_value(self, value):
        if self.test(value):
            return self.monkey_true
        else:
            return self.monkey_false


def parse_predicate(predicate_lines):
    operand = int(re.search(r'\d+', predicate_lines[0]).group(0))
    monkey_true = int(re.search(r'\d+', predicate_lines[1]).group(0))
    monkey_false = int(re.search(r'\d+', predicate_lines[2]).group(0))
    return TestPredicate(lambda x: x % operand == 0, operand, monkey_true, monkey_false)

import operator
import re

operators = {
    '*': operator.mul,
    '+': operator.add
}


def parse_operation(operation_text):
    groups = re.match(r'new = old (?P<operator>.) (?P<operand>.+)', operation_text).groupdict()
    op = operators[groups['operator']]
    operand = groups['operand']
    return lambda x: op(x, x if operand == 'old' else int(operand))

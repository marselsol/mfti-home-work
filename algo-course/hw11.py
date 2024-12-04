class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_expression_tree(expression):
    def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        if op == '^':
            return 3
        return 0

    def apply_operator(operators, operands):
        operator = operators.pop()
        right = operands.pop()
        left = operands.pop()
        node = TreeNode(operator)
        node.left = left
        node.right = right
        operands.append(node)

    operators = []
    operands = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isalnum():
            number = ""
            while i < len(expression) and expression[i].isalnum():
                number += expression[i]
                i += 1
            i -= 1
            operands.append(TreeNode(number))
        elif char == '(':
            operators.append(char)
        elif char == ')':
            while operators[-1] != '(':
                apply_operator(operators, operands)
            operators.pop()
        elif char in ('+', '-', '*', '/', '^'):
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(char)):
                apply_operator(operators, operands)
            operators.append(char)
        i += 1

    while operators:
        apply_operator(operators, operands)

    return operands[-1]


def print_tree(node, level=0, label="Root"):
    if node:
        print(" " * (level * 4) + f"{label}: {node.value}")
        print_tree(node.left, level + 1, "L")
        print_tree(node.right, level + 1, "R")


# Пример выражения: (a+b)*(c*(d+e+f))+g*(i+j^2)
expression = "(a+b)*(c*(d+e+f))+g*(i+j^2)"
tree = build_expression_tree(expression)
print_tree(tree)

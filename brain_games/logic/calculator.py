import random


def calculator():
    item1 = random.randint(1, 25)
    item2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    expression = f'{item1} {operation} {item2}'
    correct_answers_map = {
        '+': item1 + item2,
        '-': item1 - item2,
        '*': item1 * item2
    }
    answer_type = int
    return expression, correct_answers_map[operation], answer_type

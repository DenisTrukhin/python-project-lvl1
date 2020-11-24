import random


def calculate_gcd(num1, num2):
    max_num, min_num = max(num1, num2), min(num1, num2)
    while min_num != 0:
        max_num %= min_num
        max_num, min_num = min_num, max_num
    return max_num


def gcd():
    item1 = random.randint(1, 100)
    item2 = random.randint(1, 100)
    expression = f'{item1} {item2}'
    correct_answer = calculate_gcd(item1, item2)
    answer_type = int
    return expression, correct_answer, answer_type

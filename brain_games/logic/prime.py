import random


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d ** 2 <= n and n % d != 0:
        d += 2
    return d ** 2 > n


def prime():
    positive_answer = 'yes'
    negative_answer = 'no'

    number = random.randint(1, 1000)
    expression = f'{number}'
    correct_answer = positive_answer if is_prime(number) else negative_answer
    answer_type = str
    return expression, correct_answer, answer_type

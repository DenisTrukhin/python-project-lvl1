import random


def even():
    positive_answer = 'yes'
    negative_answer = 'no'

    number = random.randint(1, 99)
    is_number_even = number % 2 == 0
    correct_answer = positive_answer if is_number_even else negative_answer
    answer_type = str
    return number, correct_answer, answer_type

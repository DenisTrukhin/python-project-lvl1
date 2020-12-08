import random


def progression():
    min_progression_length = 5
    max_progression_length = 10

    step = random.randint(1, 10)
    start = random.randint(1, 30)
    end = random.randint(
        start + step * min_progression_length,
        start + step * max_progression_length
    )
    current_progression = [num for num in range(start, end, step)]
    answer_index = random.randint(0, len(current_progression) - 1)

    correct_answer = current_progression[answer_index]
    current_progression[answer_index] = '..'
    expression = ' '.join(map(str, current_progression))
    answer_type = int

    return expression, correct_answer, answer_type

import prompt
import random


POSITIVE_ANSWER = 'yes'
NEGATIVE_ANSWER = 'no'
MAX_CORRECT_ANSWERS = 3


def even(player_name):
    correct_answers_num = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while correct_answers_num < MAX_CORRECT_ANSWERS:
        number = random.randint(1, 99)
        is_number_even = number % 2 == 0
        correct_answer = POSITIVE_ANSWER if is_number_even else NEGATIVE_ANSWER
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            correct_answers_num += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {player_name}!')
            break
    if correct_answers_num == MAX_CORRECT_ANSWERS:
        print(f'Congratulations, {player_name}!')


import prompt

from brain_games.cli import welcome_user

MAX_CORRECT_ANSWERS = 3
ANSWER_TYPE_MAP = {
    int: prompt.integer,
    str: prompt.string
}


def game(greeting, get_task_items):
    player_name = welcome_user()
    correct_answers_num = 0
    print(greeting)
    while correct_answers_num < MAX_CORRECT_ANSWERS:
        question, correct_answer, correct_answer_type = get_task_items()
        print(f'Question: {question}')
        answer_prompt = ANSWER_TYPE_MAP[correct_answer_type]
        answer = answer_prompt('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            correct_answers_num += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f'Let\'s try again, {player_name}!')
            break
    if correct_answers_num == MAX_CORRECT_ANSWERS:
        print(f'Congratulations, {player_name}!')

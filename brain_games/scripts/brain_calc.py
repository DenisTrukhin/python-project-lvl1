from ..logic.base import game
from ..logic.calculator import calculator


def main():
    greeting = 'What is the result of the expression?'
    game(greeting, calculator)


if __name__ == '__main__':
    main()

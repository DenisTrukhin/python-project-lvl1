from ..logic.base import game
from ..logic.progression import progression


def main():
    greeting = 'What number is missing in the progression?'
    game(greeting, progression)


if __name__ == '__main__':
    main()

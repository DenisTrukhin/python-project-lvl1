from ..logic.base import game
from ..logic.even import even


def main():
    greeting = 'Answer "yes" if the number is even, otherwise answer "no".'
    game(greeting, even)


if __name__ == '__main__':
    main()

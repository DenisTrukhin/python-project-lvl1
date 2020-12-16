from ..logic.base import game
from ..logic.prime import prime


def main():
    greeting = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game(greeting, prime)


if __name__ == '__main__':
    main()

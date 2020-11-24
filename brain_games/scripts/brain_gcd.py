from ..logic.base import game
from ..logic.gcd import gcd


def main():
    greeting = 'Find the greatest common divisor of given numbers.'
    game(greeting, gcd)


if __name__ == '__main__':
    main()

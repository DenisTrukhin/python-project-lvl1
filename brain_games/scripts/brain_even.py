from ..cli import welcome_user
from ..logic.even import even


def main():
    name = welcome_user()
    even(name)


if __name__ == '__main__':
    main()

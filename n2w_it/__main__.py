import sys
from argparse import ArgumentParser

from n2w_it import N2W_IT

instance = N2W_IT()


def main():
    parser = ArgumentParser()
    parser.add_argument("number", nargs="?", const=1, type=str)

    args = parser.parse_args()

    try:
        result = instance.number_to_words(args.number)

        print(result)
        return 0
    except Exception as exception:
        print(exception)
        return -1


if __name__ == "__main__":
    sys.exit(main())

import sys

from UI.cli.CommandLineInterface import CommandLineInterface


def main(argv):
    if len(argv) >= 2:
        cli = CommandLineInterface(argv[0], argv[1])
        cli.release_note()
    else:
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])

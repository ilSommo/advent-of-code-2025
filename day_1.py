"""Day 1: Secret Entrance"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 1 puzzles."""
    with open("inputs/day_1.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    operations = parse_input(puzzle_input)
    dial = 50
    password = 0

    for operation in operations:
        dial = (dial + operation) % 100
        password += dial == 0

    return password


def star_2(puzzle_input):
    """Solve second puzzle."""
    operations = parse_input(puzzle_input)
    dial = 50
    password = 0

    for operation in operations:
        dial += operation
        password += abs(dial) // 100
        password += dial <= 0 and dial != operation
        dial %= 100

    return password


def parse_input(puzzle_input):
    """Convert puzzle input to numbers."""
    return tuple(
        int(line[1:]) * (1 if line[0] == "R" else -1) for line in puzzle_input
    )


if __name__ == "__main__":
    main()

"""Day 6: Trash Compactor"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"

from math import prod


def main():
    """Solve day 6 puzzles."""
    with open("inputs/day_6.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip("\n") for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    problems = parse_problems(puzzle_input)

    return compute_total(problems)


def star_2(puzzle_input):
    """Solve second puzzle."""
    problems = parse_vertical_problems(puzzle_input)

    return compute_total(problems)


def compute_total(problems):
    """Compute total result of problems."""

    return sum(
        sum(numbers) if operation == "+" else prod(numbers)
        for operation, numbers in problems
    )


def parse_problems(puzzle_input):
    """Get problem operations and number."""
    lines = [line.split() for line in puzzle_input]

    return tuple(
        (operation, tuple(int(line[i]) for line in lines[:-1]))
        for i, operation in enumerate(lines[-1])
    )


def parse_vertical_problems(puzzle_input):
    """Get problem operations and number."""
    max_length = max(len(line) for line in puzzle_input)
    lines = [line.ljust(max_length) for line in puzzle_input]

    number_lines = lines[:-1]
    operation_line = lines[-1]

    problems = [[None, []]]

    for i, char in enumerate(operation_line):
        if all(line[i] == " " for line in lines):
            problems[-1][-1] = tuple(problems[-1][-1])
            problems[-1] = tuple(problems[-1])
            problems.append([None, []])
            continue

        if char != " ":
            problems[-1][0] = char

        problems[-1][-1].append(int("".join(line[i] for line in number_lines)))

    problems[-1][-1] = tuple(problems[-1][-1])
    problems[-1] = tuple(problems[-1])

    return problems


if __name__ == "__main__":
    main()

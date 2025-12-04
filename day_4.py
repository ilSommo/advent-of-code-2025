"""Day 4: Printing Department"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"

from functools import cache
from itertools import product


def main():
    """Solve day 4 puzzles."""
    with open("inputs/day_4.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    rolls = get_rolls(puzzle_input)

    return sum(len(rolls & get_adjacent(roll)) < 4 for roll in rolls)


def star_2(puzzle_input):
    """Solve second puzzle."""
    rolls = set(get_rolls(puzzle_input))
    removed = set()

    while True:
        to_remove = {
            roll for roll in rolls if len(rolls & get_adjacent(roll)) < 4
        }

        if not to_remove:
            break

        removed |= to_remove
        rolls -= to_remove

    return len(removed)


@cache
def get_adjacent(roll):
    """Get coordinates of adjacent positions to a roll."""
    return frozenset(
        {roll + (i + j * 1j) for i, j in product((-1, 0, 1), repeat=2)}
        - {roll}
    )


def get_rolls(puzzle_input):
    """Get rolls of papers from input."""
    rolls = set()

    for i, line in enumerate(puzzle_input):
        for j, char in enumerate(line):
            if char == "@":
                rolls.add(i + j * 1j)

    return frozenset(rolls)


if __name__ == "__main__":
    main()

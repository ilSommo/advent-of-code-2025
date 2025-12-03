"""Day 3: Lobby"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 3 puzzles."""
    with open("inputs/day_3.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    banks = get_banks(puzzle_input)

    return sum(get_highest(bank, 2) for bank in banks)


def star_2(puzzle_input):
    """Solve second puzzle."""
    banks = get_banks(puzzle_input)

    return sum(get_highest(bank, 12) for bank in banks)


def get_banks(puzzle_input):
    """Get battery banks from input."""
    return tuple(tuple(map(int, line)) for line in puzzle_input)


def get_highest(bank, length):
    """Get highest possible value of given length."""
    i = 0
    j = length - 1

    digits = []

    while j >= 1:
        digits.insert(0, max(bank[i:-j]))
        i += bank[i:-j].index(digits[0]) + 1
        j -= 1

    digits.insert(0, max(bank[i:]))

    return sum(10**i * digit for i, digit in enumerate(digits))


if __name__ == "__main__":
    main()

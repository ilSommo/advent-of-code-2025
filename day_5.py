"""Day 5: Cafeteria"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 5 puzzles."""
    with open("inputs/day_5.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    ranges, ids = parse_input(puzzle_input)

    return sum(
        any(start <= id_ <= end for start, end in ranges) for id_ in ids
    )


def star_2(puzzle_input):
    """Solve second puzzle."""
    ranges, _ = parse_input(puzzle_input)
    ranges = sorted(ranges, key=lambda x: x[0])
    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))

        else:
            merged.append((start, end))

    return sum(end - start + 1 for start, end in merged)


def parse_input(puzzle_input):
    """Parse puzzle input."""
    blank = puzzle_input.index("")

    ranges = tuple(
        tuple(map(int, line.split("-"))) for line in puzzle_input[:blank]
    )
    ids = tuple(map(int, puzzle_input[blank + 1 :]))

    return ranges, ids


if __name__ == "__main__":
    main()

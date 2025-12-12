"""Day 12: Christmas Tree Farm"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"


from math import prod


def main():
    """Solve day 12 puzzles."""
    with open("inputs/day_12.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    shapes, regions = parse_input(puzzle_input)

    return sum(
        sum(
            len(shape) * quantity
            for shape, quantity in zip(shapes, quantities)
        )
        < prod(dimensions)
        for dimensions, quantities in regions
    )


def parse_input(puzzle_input):
    """Parse puzzle input."""
    breaks = [i for i, line in enumerate(puzzle_input) if line == ""]

    shapes = []

    start = 1

    for end in breaks:
        shapes.append(
            {
                i + j * 1j
                for i, line in enumerate(puzzle_input[start:end])
                for j, char in enumerate(line)
                if char == "#"
            }
        )
        start = end + 1

    regions = []

    for line in puzzle_input[start:]:
        dimensions, quantities = line.split(": ")
        regions.append(
            (
                tuple(map(int, dimensions.split("x"))),
                tuple(map(int, quantities.split(" "))),
            )
        )

    return tuple(shapes), tuple(regions)


if __name__ == "__main__":
    main()

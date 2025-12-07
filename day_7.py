"""Day 7: Laboratories"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"

from collections import defaultdict


def main():
    """Solve day 7 puzzles."""
    with open("inputs/day_7.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    start, splitters = parse_diagram(puzzle_input)
    beams = {start}

    splits = 0

    for line in splitters:
        new_beams = set()

        for beam in beams:
            if beam in line:
                splits += 1
                new_beams |= {beam - 1, beam + 1}
            else:
                new_beams.add(beam)

        beams = new_beams

    return splits


def star_2(puzzle_input):
    """Solve second puzzle."""
    start, splitters = parse_diagram(puzzle_input)
    beams = {start: 1}

    for line in splitters:
        new_beams = defaultdict(int)

        for beam, count in beams.items():
            if beam in line:
                new_beams[beam - 1] += count
                new_beams[beam + 1] += count
            else:
                new_beams[beam] += count

        beams = new_beams

    return sum(beams.values())


def parse_diagram(puzzle_input):
    """Get start and splitters."""
    start = puzzle_input[0].index("S")
    splitters = tuple(
        tuple(i for i, char in enumerate(line) if char == "^")
        for line in puzzle_input[2::2]
    )

    return start, splitters


if __name__ == "__main__":
    main()

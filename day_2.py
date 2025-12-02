"""Day 2: Gift Shop"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 2 puzzles."""
    with open("inputs/day_2.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    id_ranges = get_id_ranges(puzzle_input)
    invalid_ids = []

    for id_range in id_ranges:
        for id_ in id_range:
            id_string = str(id_)

            if (
                len(id_string) % 2 == 0
                and id_string[: len(id_string) // 2]
                == id_string[len(id_string) // 2 :]
            ):
                invalid_ids.append(id_)

    return sum(invalid_ids)


def star_2(puzzle_input):
    """Solve second puzzle."""
    id_ranges = get_id_ranges(puzzle_input)
    invalid_ids = []

    for id_range in id_ranges:
        for id_ in id_range:
            id_string = str(id_)

            for sub_len in range(1, len(id_string) // 2 + 1):
                if (
                    len(id_string) % sub_len == 0
                    and id_string[:sub_len] * (len(id_string) // sub_len)
                    == id_string
                ):
                    invalid_ids.append(id_)
                    break

    return sum(invalid_ids)


def get_id_ranges(puzzle_input):
    """Get ID ranges from puzzle input."""
    id_ranges = []

    for id_range in puzzle_input.split(","):
        start, end = map(int, id_range.split("-"))
        id_ranges.append(range(start, end + 1))

    return tuple(id_ranges)


if __name__ == "__main__":
    main()

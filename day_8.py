"""Day 8: Playground"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"

from functools import cache
from itertools import combinations
from math import dist


def main():
    """Solve day 8 puzzles."""
    with open("inputs/day_8.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    boxes = get_boxes(puzzle_input)

    order = compute_order(boxes)

    circuits = tuple(frozenset({box}) for box in boxes)

    for box_0, box_1 in order[:1000]:
        circuits = update_circuits(circuits, box_0, box_1)

    circuits = sorted(circuits, key=len, reverse=True)

    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])


def star_2(puzzle_input):
    """Solve second puzzle."""
    boxes = get_boxes(puzzle_input)

    order = compute_order(boxes)

    circuits = tuple(frozenset({box}) for box in boxes)

    for box_0, box_1 in order:
        circuits = update_circuits(circuits, box_0, box_1)

        if len(circuits) == 1:
            return box_0[0] * box_1[0]

    return None


@cache
def compute_order(boxes):
    """Compute connection order of boxes."""
    return tuple(
        box_pair
        for distance, box_pair in sorted(
            (dist(box_0, box_1), frozenset({box_0, box_1}))
            for box_0, box_1 in combinations(boxes, 2)
        )
    )


def get_boxes(puzzle_input):
    """Get boxes from input."""
    return frozenset(tuple(map(int, line.split(","))) for line in puzzle_input)


@cache
def update_circuits(circuits, box_0, box_1):
    """Update circuits by connecting the given boxes."""
    circuits_ = list(circuits)
    i_0 = i_1 = None

    for i, circuit in enumerate(circuits_):
        if box_0 in circuit:
            i_0 = i

        if box_1 in circuit:
            i_1 = i

        if i_0 is not None and i_1 is not None:
            break

    if i_0 == i_1:
        pass
    else:
        i_min = min(i_0, i_1)
        i_max = max(i_0, i_1)
        circuits_[i_min] = circuits_[i_min] | circuits_.pop(i_max)

    return tuple(circuits_)


if __name__ == "__main__":
    main()

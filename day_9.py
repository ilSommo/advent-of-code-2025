"""Day 9: Movie Theater"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"

from itertools import combinations


def main():
    """Solve day 9 puzzles."""
    with open("inputs/day_9.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    tiles = get_tiles(puzzle_input)

    return int(
        max(
            (abs(tile_0.real - tile_1.real) + 1)
            * (abs(tile_0.imag - tile_1.imag) + 1)
            for tile_0, tile_1 in combinations(tiles, 2)
        )
    )


def star_2(puzzle_input):
    """Solve second puzzle."""
    tiles = get_tiles(puzzle_input)

    max_area = 0
    border = compute_border(tiles)

    for tile_0, tile_1 in combinations(tiles, 2):
        min_i = int(min(tile_0.real, tile_1.real))
        max_i = int(max(tile_0.real, tile_1.real))
        min_j = int(min(tile_0.imag, tile_1.imag))
        max_j = int(max(tile_0.imag, tile_1.imag))

        area = (max_i - min_i + 1) * (max_j - min_j + 1)

        if area <= max_area:
            continue

        if any(
            min_i < tile.real < max_i and min_j < tile.imag < max_j
            for tile in border
        ):
            continue

        mid_point = (max_i + min_i) // 2 + (max_j + min_j) // 2 * 1j

        if is_internal(mid_point, border):
            max_area = area

    return max_area


def compute_border(tiles):
    """Compute location of border starting from tiles."""
    border = set(tiles)

    for tile_0, tile_1 in zip(tiles, tiles[1:] + tiles[:1]):
        border |= compute_connection(tile_0, tile_1)

    return frozenset(border)


def compute_connection(tile_0, tile_1):
    """Compute connection between two tiles."""
    if tile_0.real == tile_1.real:
        j_min = int(min(tile_0.imag, tile_1.imag))
        j_max = int(max(tile_0.imag, tile_1.imag))
        connection = frozenset(
            {tile_0.real + j * 1j for j in range(j_min + 1, j_max)}
        )
    else:
        i_min = int(min(tile_0.real, tile_1.real))
        i_max = int(max(tile_0.real, tile_1.real))
        connection = frozenset(
            {i + tile_0.imag * 1j for i in range(i_min + 1, i_max)}
        )

    return connection


def get_tiles(puzzle_input):
    """Get tile coordinates from input."""
    return tuple(complex(*map(int, line.split(","))) for line in puzzle_input)


def is_internal(point, border):
    """Check if a point is inside a border."""
    x, y = int(point.real), int(point.imag)

    edge = False
    inside = False

    for i in range(x + 1):
        if i + y * 1j in border and edge is False:
            edge = True

        elif i + y * 1j not in border and edge is True:
            edge = False
            inside = not inside

    return inside


if __name__ == "__main__":
    main()

"""Day 11: Reactor"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"

from functools import cache


def main():
    """Solve day 11 puzzles."""
    with open("inputs/day_11.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    devices = get_devices(puzzle_input)

    return count_paths("you", "out", devices)


def star_2(puzzle_input):
    """Solve second puzzle."""
    devices = get_devices(puzzle_input)

    return count_paths_dac_fft("svr", "out", devices, False, False)


@cache
def count_paths(input_, output, devices):
    """Count paths from input to output."""
    if input_ == output:
        return 1

    return sum(
        count_paths(device, output, devices)
        for device in dict(devices)[input_]
    )


@cache
def count_paths_dac_fft(input_, output, devices, dac, fft):
    """Count paths from input to output."""
    if input_ == output:
        return dac and fft

    dac = dac or input_ == "dac"
    fft = fft or input_ == "fft"

    return sum(
        count_paths_dac_fft(device, output, devices, dac, fft)
        for device in dict(devices)[input_]
    )


def get_devices(puzzle_input):
    """Get devices from input."""
    devices = {}

    for line in puzzle_input:
        device, outputs = line.split(": ")
        devices[device] = tuple(outputs.split(" "))

    return tuple(devices.items())


if __name__ == "__main__":
    main()

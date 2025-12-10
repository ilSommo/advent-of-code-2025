"""Day 10: Factory"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"

from collections import deque

from scipy.optimize import linprog


def main():
    """Solve day 10 puzzles."""
    with open("inputs/day_10.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    diagrams, schematics, _ = parse_manual(puzzle_input)

    return sum(
        compute_minimum_presses_diagram(diagram, buttons)
        for diagram, buttons in zip(diagrams, schematics)
    )


def star_2(puzzle_input):
    """Solve second puzzle."""
    _, schematics, requirements = parse_manual(puzzle_input)

    return sum(
        compute_minimum_presses_requirement(requirement, buttons)
        for requirement, buttons in zip(requirements, schematics)
    )


def compute_minimum_presses_diagram(diagram, buttons):
    """Compute minimum number of presses for given diagram and buttons."""
    initial_state = (False,) * len(diagram)
    states = {initial_state}
    current_states = deque([(initial_state, 0)])

    while True:
        current_state, presses = current_states.popleft()
        presses += 1

        for button in buttons:
            state = press_button(current_state, button)

            if state == diagram:
                return presses

            if state not in states:
                states.add(state)
                current_states.append((state, presses))

    return None


def compute_minimum_presses_requirement(requirement, buttons):
    """Compute minimum number of presses for given requirement and buttons."""
    A = [
        [1 if i in button else 0 for button in buttons]
        for i in range(len(requirement))
    ]

    return round(
        linprog(
            c=[1] * len(buttons), A_eq=A, b_eq=requirement, integrality=1
        ).fun
    )


def parse_manual(puzzle_input):
    """Get diagrams, schematics, and requirements from input."""
    diagrams = []
    schematics = []
    requirements = []

    for line in puzzle_input:
        i = line.index("]")
        j = line.index("{")

        diagrams.append(tuple(char == "#" for char in line[1:i]))
        schematics.append(
            tuple(
                tuple(map(int, schematic.split(",")))
                for schematic in line[i + 3 : j - 2].split(") (")
            )
        )
        requirements.append(tuple(map(int, line[j + 1 : -1].split(","))))

    return tuple(diagrams), tuple(schematics), tuple(requirements)


def press_button(state, button):
    """Press a button."""
    return tuple(
        not indicator if i in button else indicator
        for i, indicator in enumerate(state)
    )


if __name__ == "__main__":
    main()

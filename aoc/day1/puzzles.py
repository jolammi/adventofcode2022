from pathlib import Path


def read_input(is_example: bool = False) -> str:
    input_file = "input.txt" if not is_example else "_input.txt"
    with open(Path(__file__).parent / input_file) as handle:
        return handle.read()


def parse_input(data: str) -> list[str]:
    """First modifications for data before parsing, e.g. split by lines"""
    return data.splitlines()


def _get_elves_calories(data: list[str]) -> list[int]:
    """
    Calculates total calories carried by each elf. Returns a list of elves' calories.
    """
    data.append("")
    new_list = []
    sublist = []
    for val in data:
        if val:
            sublist.append(val)
        else:
            new_list.append(sublist)
            sublist = []
            continue

    int_data = [[int(x) for x in subl] for subl in new_list]

    calories = [sum(subl) for subl in int_data]
    return calories


def puzzle1(data: list[str]) -> int:
    """Finds the biggest amount of calories from the list of the elves' calories."""
    elves = _get_elves_calories(data)
    max_val = max(elves)
    return max_val


def puzzle2(data: list[str]) -> int:
    """Sums the tree biggest calorie amount in the elves' calories list."""
    elves = _get_elves_calories(data)
    elves.sort(reverse=True)
    val = sum(elves[:3])
    return val


def _assert1(answer1: int, is_example: bool) -> None:
    """Asserts that the answer1 is as it should be, for e.g. refactoring."""
    if is_example:
        assert answer1 == 24000  # example data
    else:
        assert answer1 == 71934


def _assert2(answer2: int, is_example: bool) -> None:
    """Asserts that the answer2 is as it should be, for e.g. refactoring."""
    if is_example:
        assert answer2 == 45000  # example data
    else:
        assert answer2 == 211447


if __name__ == "__main__":
    is_example = False

    data = parse_input(read_input(is_example=is_example))

    answer1 = puzzle1(data)
    _assert1(answer1, is_example)
    print(f"The eld with the biggest calorie amount carries {answer1} calories")

    answer2 = puzzle2(data)
    _assert2(answer2, is_example)
    print(f"Three elves with most calories carry a total of {answer2} calories")

from pathlib import Path
import re


def read_input(is_example: bool = False) -> str:
    input_file = "input.txt" if not is_example else "_input.txt"
    with open(Path(__file__).parent / input_file) as handle:
        return handle.read()


def parse_input(data: str) -> list[list[tuple[int, int]]]:
    """
    Parses data to list of sublists that contain two two-integer tuples
    e.g.
    2-4,6-8
    2-3,4-5
    -->
    [[('2', '4'), ('6', '8')], [('2', '3'), ('4', '5')]]
    """
    output = []
    data_split = data.splitlines()
    # regex pattern to parse <num>-<num>,<num>-<num>
    regex = r"(?P<t1_num1>^\d+)-(?P<t1_num2>\d+),(?P<t2_num1>\d+)-(?P<t2_num2>\d+)$"
    for line in data_split:
        match = re.match(regex, line)
        if not match:
            raise Exception("Malformed data, check input files")
        output.append(
            [
                (int(match["t1_num1"]), int(match["t1_num2"])),
                (int(match["t2_num1"]), int(match["t2_num2"])),
            ]
        )

    return output


def one_contains_other(line: list[tuple[int, int]]) -> bool:
    """Returns True if one tuple contains another, otherwise False."""
    (start1, end1), (start2, end2) = line
    if (start1 <= start2) and (end1 >= end2):
        return True
    elif (start2 <= start1) and (end2 >= end1):
        return True
    return False


def one_overlaps_other(line: list[tuple[int, int]]) -> bool:
    """Returns True if one tuple overlaps another, otherwise False."""
    (start1, end1), (start2, end2) = line
    if (start1 <= start2) and (end1 >= start2):
        return True
    elif (start2 <= start1) and (end2 >= start1):
        return True
    return False


def puzzle1(data: list[list[tuple[int, int]]]) -> int:
    """Counts total cases where one tuple of a row contains the other."""
    total_contains = 0
    for line in data:
        if one_contains_other(line):
            total_contains += 1
    return total_contains


def puzzle2(data: list[list[tuple[int, int]]]) -> int:
    """Counts total cases where one tuple of a row overlaps the other."""
    total_contains = 0
    for line in data:
        if one_overlaps_other(line):
            total_contains += 1
    return total_contains


def _assert1(answer1: int, is_example: bool) -> None:
    """Asserts that the answer1 is as it should be, for e.g. refactoring."""
    if is_example:
        assert answer1 == 2  # example data
    else:
        assert answer1 == 500


def _assert2(answer2: int, is_example: bool) -> None:
    """Asserts that the answer2 is as it should be, for e.g. refactoring."""
    if is_example:
        assert answer2 == 2  # example data
    else:
        assert answer2 == 815


if __name__ == "__main__":
    is_example = False

    data = parse_input(read_input(is_example=is_example))

    answer1 = puzzle1(data)
    print(f"One range fully contains the other in {answer1} assignment pairs")
    _assert1(answer1, is_example)

    answer2 = puzzle2(data)
    print(f"Ranges overlap in {answer2} assignment pairs")
    _assert2(answer2, is_example)

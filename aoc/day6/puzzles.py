from pathlib import Path
from typing import Any


def read_input(is_example: bool = False) -> str:
    """
    Reads the input file based on whether example is wanted or not.
    Returns input as a string.
    """
    input_file = "input.txt" if not is_example else "_input.txt"
    with open(Path(__file__).parent / input_file) as handle:
        return handle.read()


def puzzle(data: Any, window_size: int) -> Any:
    """
    Takes a slice of the data and puts it in a set. If the set length is the same as
    the window length, all characters are unique and the window of characters before the
    current character is the start-of-packet (puzzle1) / start-of-message (puzzle2)
    marker.
    """
    for idx in range(window_size - 1, len(data)):
        window = set(data[idx - window_size + 1 : idx + 1])
        if len(window) == window_size:
            # counting chars starts from 1 but lists start from 0
            return idx + 1


def _assert1(answer1: int, is_example: bool) -> None:
    """Asserts that the answer1 is as it should be, for e.g. refactoring."""
    if is_example:
        assert answer1 == 7  # example data
        pass
    else:
        assert answer1 == 1155
        pass


def _assert2(answer2: int, is_example: bool) -> None:
    """Asserts that the answer2 is as it should be, for e.g. refactoring."""
    if is_example:
        assert answer2 == 19  # example data
    else:
        assert answer2 == 2789


if __name__ == "__main__":
    is_example = False

    data = read_input(is_example=is_example)

    answer1 = puzzle(data, window_size=4)
    print(
        f"The first start-of-packet marker is detected after processing {answer1} characters."
    )
    _assert1(answer1, is_example)

    answer2 = puzzle(data, window_size=14)
    print(
        f"The first start-of-packet marker is detected after processing {answer2} characters."
    )
    _assert2(answer2, is_example)

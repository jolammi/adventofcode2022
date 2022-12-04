from pathlib import Path
from typing import Any


def read_input(is_example: bool = False) -> str:
    input_file = "input.txt" if not is_example else "_input.txt"
    with open(Path(__file__).parent / input_file) as handle:
        return handle.read()


def parse_input(data: str) -> Any:
    """ """
    return data


def do_stuff(data: Any) -> Any:
    """ """
    pass


def puzzle1(data: Any) -> Any:
    """ """
    val = do_stuff(data)
    return val


def puzzle2(data: Any) -> Any:
    """ """
    val = do_stuff(data)
    return val


def _assert1(answer1: int, is_example: bool) -> None:
    """Asserts that the answer1 is as it should be, for e.g. refactoring."""
    if is_example:
        # assert answer1 == 0  # example data
        pass
    else:
        # assert answer1 == 0
        pass


def _assert2(answer2: int, is_example: bool) -> None:
    """Asserts that the answer2 is as it should be, for e.g. refactoring."""
    if is_example:
        # assert answer2 == 0  # example data
        pass
    else:
        # assert answer2 == 0
        pass


if __name__ == "__main__":
    is_example = True

    data = parse_input(read_input(is_example=is_example))

    answer1 = puzzle1(data)
    print(f"{answer1}")
    _assert1(answer1, is_example)

    answer2 = puzzle2(data)
    print(f"{answer2}")
    _assert2(answer2, is_example)

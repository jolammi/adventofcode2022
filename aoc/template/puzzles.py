from pathlib import Path
from aoc.utils.utils import read_input_as_lines_list

def format_data(data: list[str]) -> list[int]:
    print(data)
    pass

def puzzle1(data: list[int]) -> int:
    """
    Placeholder
    """
    pass

def puzzle2(data: list[str]) -> int:
    """
    Placeholder
    """
    pass

if __name__ == "__main__":
    data = format_data(read_input_as_lines_list(__file__, example=True))
    answer = puzzle1(data)
    # assert answer ==
    # assert answer ==   # example data
    print(f"{answer}")
    answer2 = puzzle2(data)
    # assert answer2 ==
    # assert answer2 ==   # example data
    print(f"{answer2}")
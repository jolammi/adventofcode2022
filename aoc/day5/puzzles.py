import re
from copy import deepcopy
from pathlib import Path

INSTR_REGEX = r"^move (?P<container_num>\d+) from (?P<from>\d+) to (?P<to>\d+)$"


def read_input(is_example: bool = False) -> str:
    """
    Reads the input file based on whether example is wanted or not.
    Returns input as a string.
    """
    input_file = "input.txt" if not is_example else "_input.txt"
    with open(Path(__file__).parent / input_file) as handle:
        return handle.read()


def parse_input(data: str) -> tuple[list[list[str]], list[tuple[int, int, int]]]:
    """
    Parses input and returns two lists.
    The first list has the containers as lists of strings. The lists are built as
    columns, so that the first element of every list is the topmost container of each
    tower.

    The second list has the instructions as three-element tuples:
    (amount of containers to move, strack to move from, stack to move to).
    """
    instructions = []
    containers_str, instructions_str = data.split("\n\n")
    containers = []
    length = int(containers_str.splitlines().pop(-1).split("   ")[-1])
    rows = containers_str.splitlines()[:-1]
    for line in rows:
        subl = []
        for i in range(1, length * 4, 4):
            try:
                if line[i].isalpha():
                    subl.append(line[i])
                else:
                    subl.append("")
            # I have global whitespace stripping on so this is because of that
            except IndexError:
                subl.append("")
        containers.append(subl)
    containers = list(map(list, zip(*containers)))
    containers = [[i for i in subl if i] for subl in containers]

    for line in instructions_str.splitlines():
        match = re.match(INSTR_REGEX, line)
        if not match:
            raise Exception("Malformed data, check inputs")
        instructions.append(
            (int(match["container_num"]), int(match["from"]), int(match["to"]))
        )

    return containers, instructions


def puzzle(
    containers: list[list[str]],
    instructions: list[tuple[int, int, int]],
    reverse: bool = False,
) -> str:
    """
    Solves the puzzle by moving the containers as instructed.
    In the first puzzle the chunk to move is reversed, as if the containers were
    moved one by one. In the second part the chunk is not reversed, as the containers
    are moved in a stack.
    Returns the letters of the topmost containers as a word.
    """
    for amount, _from, _to in instructions:
        chunk = containers[_from - 1][:amount]
        if reverse:
            chunk.reverse()
        [containers[_from - 1].pop(0) for _ in range(amount)]
        chunk.extend(containers[_to - 1])
        containers[_to - 1] = chunk

    val = "".join(x[0] for x in containers)
    return val


def _assert1(answer1: str, is_example: bool) -> None:
    """Asserts that the answer1 is as it should be, for e.g. refactoring."""
    if is_example:
        assert answer1 == "CMZ"  # example data
    else:
        assert answer1 == "HNSNMTLHQ"


def _assert2(answer2: str, is_example: bool) -> None:
    """Asserts that the answer2 is as it should be, for e.g. refactoring."""
    if is_example:
        assert answer2 == "MCD"  # example data
    else:
        assert answer2 == "RNLFDJMCT"


if __name__ == "__main__":
    is_example = False

    containers, instructions = parse_input(read_input(is_example=is_example))
    containers2 = deepcopy(containers)

    answer1 = puzzle(containers, instructions, reverse=True)
    print(f"The order of top crates is {answer1}")
    _assert1(answer1, is_example)

    answer2 = puzzle(containers2, instructions)
    print(f"The order of top crates is {answer2}")
    _assert2(answer2, is_example)

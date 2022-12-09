from pathlib import Path


def read_input(is_example: bool = False) -> str:
    """
    Reads the input file based on whether example is wanted or not.
    Returns input as a string.
    """
    input_file = "input.txt" if not is_example else "_input.txt"
    with open(Path(__file__).parent / input_file) as handle:
        return handle.read()


def parse_input(data: str) -> list[list[int]]:
    """Parses input to list of lists of integers."""
    output = data.splitlines()
    output = [[int(i) for i in subl] for subl in output]
    return output


def is_visible(row: list[int], idx: int) -> bool:
    """
    Returns true if given index of a row is visible from outside the grid.
    If any tree between the current tree and the beginning of the row is as high or
    taller than the current tree, returns False, else True."""
    if not any([x >= row[idx] for x in row[:idx]]):
        return True
    return False


def get_visible_coords_for_row(
    row: list[int], row_idx: int, flipped: bool = False
) -> set[tuple[int, int]]:
    """
    Calculates visible trees for one row and for its reversed version.
    Generates a set of coordinates that mark trees that are visible from outside
    the grid.
    This function could be written shorter but it's late and I want to sleep,
    so it'll do for now.
    """
    coords = set()
    for idx in range(len((row))):
        if idx == 0:
            continue
        if is_visible(row, idx):
            if not flipped:
                coords.add((row_idx, idx))
            else:
                coords.add((idx, row_idx))

    reversed_row = list(reversed(row))
    for idx in range(len((reversed_row))):
        curr_actual_idx = len(row) - 1 - idx
        if idx == 0:
            continue
        if is_visible(reversed_row, idx):
            if not flipped:
                coords.add((row_idx, curr_actual_idx))
            else:
                coords.add((curr_actual_idx, row_idx))
    return coords


def puzzle1(data: list[list[int]]) -> int:
    """Calculates the trees that are visible from ouside the grid."""
    visible_coords = set()
    flipped = list(map(list, zip(*data)))
    for row_idx, row in enumerate(data):
        for col_idx in range(len(row)):
            if (
                row_idx == 0
                or col_idx == 0
                or row_idx == (len(data) - 1)
                or (col_idx == len(data[0]) - 1)
            ):
                visible_coords.add((row_idx, col_idx))
                continue
        visible_coords.update(get_visible_coords_for_row(row, row_idx))

    for flipped_idx, flipped_row in enumerate(flipped):
        visible_coords.update(
            get_visible_coords_for_row(flipped_row, flipped_idx, flipped=True)
        )

    return len(visible_coords)


def get_viewing_distance(chunk, curr_val):
    """Calculates the distance to the nearest as high or taller tree."""
    dist = 0
    for val in chunk:
        dist += 1
        if val >= curr_val:
            break
    return dist


def puzzle2(data: list[list[int]]) -> int:
    """Calculates the highest scenic score from the grid."""
    best = 1
    for row_idx, row in enumerate(data):
        for col_idx, height in enumerate(row):
            curr = 1

            col = [r[col_idx] for r in data]
            up_ = list(reversed(col[:row_idx]))
            down_ = col[row_idx + 1 :]
            right = row[col_idx + 1 :]
            left = list(reversed(row[:col_idx]))

            for chunk in [up_, down_, left, right]:
                curr *= get_viewing_distance(chunk, data[row_idx][col_idx])
            if curr > best:
                best = curr
    return best


def _assert1(answer1: int, is_example: bool) -> None:
    """Asserts that the answer1 is as it should be, for e.g. refactoring."""
    if is_example:
        assert answer1 == 21  # example data
        pass
    else:
        assert answer1 == 1711
        pass


def _assert2(answer2: int, is_example: bool) -> None:
    """Asserts that the answer2 is as it should be, for e.g. refactoring."""
    if is_example:
        assert answer2 == 8  # example data
        pass
    else:
        assert answer2 == 301392
        pass


if __name__ == "__main__":
    is_example = False

    data = parse_input(read_input(is_example=is_example))

    answer1 = puzzle1(data)
    print(f"{answer1} trees are visible from outside the grid")
    _assert1(answer1, is_example)

    answer2 = puzzle2(data)
    print(f"The highest scenic score is {answer2}")
    _assert2(answer2, is_example)

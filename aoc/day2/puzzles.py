from pathlib import Path


def read_input(is_example: bool = False) -> str:
    input_file = "input.txt" if not is_example else "_input.txt"
    with open(Path(__file__).parent / input_file) as handle:
        return handle.read()


def parse_input(data: str) -> list[list[str]]:
    """
    Generate a list of list out of the data.
    Each sublist has two elements of type str.
    """
    output = data.splitlines()
    output = [line.split(" ") for line in output]
    return output


def single_game_points_1(opp_pick: str, my_pick: str):
    """Calculates the total points given from one round."""
    # X means rock; Y means paper; Z means scissors.
    my_pick_pts = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    # Top level keys mark the opponent's pick, subkeys mean my pick.
    # The values mean how many points I get with each my pick as I either win, lose or
    # draw the round.
    result_pts = {
        "A": {
            "X": 3,
            "Y": 6,
            "Z": 0,
        },
        "B": {
            "X": 0,
            "Y": 3,
            "Z": 6,
        },
        "C": {
            "X": 6,
            "Y": 0,
            "Z": 3,
        },
    }

    # Total points of a round come from the points given from my pick and
    # from the result of the round.
    total_points = my_pick_pts[my_pick] + result_pts[opp_pick][my_pick]
    return total_points


def single_game_points_2(opp_pick: str, desired_result: str):
    """Calculates the total points given from one round."""
    # X is a loss; Y is a draw; Z is a win.
    result_pts = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }
    # Top level keys mark the opponent's pick, subkeys mean the desired result.
    # The values mean how many points I get when I pick the shape that brings the
    # desired result.
    my_pick_pts = {
        "A": {
            "X": 3,
            "Y": 1,
            "Z": 2,
        },
        "B": {
            "X": 1,
            "Y": 2,
            "Z": 3,
        },
        "C": {
            "X": 2,
            "Y": 3,
            "Z": 1,
        },
    }
    # Total points of a round come from the points given from my pick and
    # from the result of the round.
    total_points = my_pick_pts[opp_pick][desired_result] + result_pts[desired_result]
    return total_points


def puzzle1(data: list[list[str]]) -> int:
    """Solve puzzle 1. Data rows have two elements, opponent's pick and my pick."""
    total_pts = 0
    for opp_pick, my_pick in data:
        total_pts = total_pts + single_game_points_1(opp_pick, my_pick)
    return total_pts


def puzzle2(data: list[list[str]]) -> int:
    """
    Solve puzzle 2. Data rows have two elements, opponent's pick and the desired result.
    """

    total_pts = 0
    for opp_pick, desired_result in data:
        total_pts = total_pts + single_game_points_2(opp_pick, desired_result)
    return total_pts


def _assert1(answer1: int, is_example: bool) -> None:
    """Asserts that the answer1 is as it should be, for e.g. refactoring."""
    if is_example:
        assert answer1 == 15  # example data
    else:
        assert answer1 == 15632


def _assert2(answer2: int, is_example: bool) -> None:
    """Asserts that the answer2 is as it should be, for e.g. refactoring."""
    if is_example:
        assert answer2 == 12  # example data
    else:
        assert answer2 == 14416


if __name__ == "__main__":
    is_example = False

    data = parse_input(read_input(is_example=is_example))
    answer1 = puzzle1(data)
    print(f"My total score would be {answer1}")
    _assert1(answer1, is_example)

    answer2 = puzzle2(data)
    print(f"My total score would be {answer2}")
    _assert2(answer2, is_example)

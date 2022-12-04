from pathlib import Path


def read_input(is_example: bool = False) -> str:
    """Reads the input into a string."""
    input_file = "input.txt" if not is_example else "_input.txt"
    with open(Path(__file__).parent / input_file) as handle:
        return handle.read()


def parse_input(data: str) -> list[str]:
    """Common parsing for data"""
    return data.splitlines()


def get_priority(char) -> int:
    """
    Returns the priority for an item type.
    a-z --> 1-26
    A-Z --> 27-52
    """
    offset = 0
    if char.isupper():
        offset = 26
    # The alphabet can be translated to numbers by taking ord(char)
    # (character's Unicode code point) and substracting 96 from it.
    return offset + ord(char.lower()) - 96


def parse_data_for_1(data) -> list[list[str]]:
    """Splits each row in half and adds the halfs as a sublist to another list."""
    output = []
    for line in data:
        subl = []
        length = len(line)
        subl.append(line[: int(length / 2)])
        subl.append(line[int(length / 2) :])
        output.append(subl)
    # print(output)
    return output


def parse_data_for_2(data) -> list[list[str]]:
    """Returns data as a list of sublists; each sublist has 3 rows of data in them."""
    output = []
    for idx in range(len(data)):
        if (idx + 1) % 3 == 0:
            output.append(data[idx - 2 : idx + 1])
    return output


def puzzle1(data: list[str]) -> int:
    """
    Parses the data into chunks of two row halfs, gets the common character from those
    two strings, gets a priority number for the character and sums the priority
    numbers of all characters.
    """
    parsed_data = parse_data_for_1(data)
    priority_sum = 0
    for half1, half2 in parsed_data:
        res = set(half1).intersection(half2).pop()
        priority = get_priority(res)
        priority_sum += priority
    return priority_sum


def puzzle2(data: list[str]) -> int:
    """
    Parses the data into chunks of three row strings, gets the common character from the
    three strings, gets a priority number for the character and sums the priority
    numbers of all characters.
    """
    parsed_data = parse_data_for_2(data)
    priority_sum = 0
    for elf1, elf2, elf3 in parsed_data:
        res = set(elf1).intersection(elf2).intersection(elf3).pop()
        priority = get_priority(res)
        priority_sum += priority
    return priority_sum


def _assert1(answer1: int, is_example: bool) -> None:
    """Asserts that the answer1 is as it should be, for e.g. refactoring."""
    if is_example:
        assert answer1 == 157  # example data
        pass
    else:
        assert answer1 == 7742
        pass


def _assert2(answer2: int, is_example: bool) -> None:
    """Asserts that the answer2 is as it should be, for e.g. refactoring."""
    if is_example:
        assert answer2 == 70  # example data
        pass
    else:
        assert answer2 == 2276
        pass


if __name__ == "__main__":
    is_example = False

    data = parse_input(read_input(is_example=is_example))

    answer1 = puzzle1(data)
    print(f"The sum of the priorities of the item types is {answer1}")
    _assert1(answer1, is_example)

    answer2 = puzzle2(data)
    print(f"The sum of the priorities of the item types is {answer2}")
    _assert2(answer2, is_example)

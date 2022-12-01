from pathlib import Path

def read_input_as_lines_list(caller_path: str, example: bool = False) -> list[str]:
    input_file = "input.txt" if not example else "_input.txt"
    with open(Path(caller_path).parent / input_file) as handle:
        return handle.read().splitlines()

def read_input_as_full_text(caller_path: str, example: bool = False) -> str:
    input_file = "input.txt" if not example else "_input.txt"
    with open(Path(caller_path).parent / input_file) as handle:
        return handle.read()
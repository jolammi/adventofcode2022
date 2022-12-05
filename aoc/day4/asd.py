def vals(a):
    b = a.split("-")
    return set(range(int(b[0]), int(b[1]) + 1))


def solve(data):
    pairs = [d.split(",") for d in data.split("\n")]
    print(pairs)
    for x, y in pairs:
        print(vals(x))
        print(vals(y))
    return sum([vals(x) >= vals(y) or vals(x) <= vals(y) for x, y in pairs])


def solve2(data):
    pairs = [d.split(",") for d in data.split("\n")]
    return sum([bool(vals(x) & vals(y)) for x, y in pairs])


if __name__ == "__main__":
    with open("_input.txt") as f:
        data = f.read()
        print(solve(data))
        print(solve2(data))

def read_input_file(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf8") as fin:
        inp = fin.readlines()

    # Strip spaces and ignore any empty lines
    inp = [line.strip() for line in inp if line.strip()]

    # Ensure all lines have the same length
    max_len = max(len(line) for line in inp)
    inp = [line.ljust(max_len) for line in inp]  # Padding shorter lines if necessary

    return inp


def parse_input(inp: list[str]) -> tuple[int, int, dict[str, list[int]]]:
    M = {}
    h, w = len(inp), len(inp[0])

    for i in range(h):
        for j in range(w):
            if (c := inp[i][j]) != ".":
                if c in M:
                    M[c].append((i, j))
                else:
                    M[c] = [(i, j)]

    return h, w, M


def part1(inp: list[str]) -> int:
    h, w, M = parse_input(inp)

    def gen_antinode(p1: tuple[int], p2: tuple[int]) -> list[tuple[int]]: 
        x1, y1 = p1
        x2, y2 = p2

        a1 = (x1 + x1 - x2, y1 + y1 - y2)
        a2 = (x2 + x2 - x1, y2 + y2 - y1)

        return [a1, a2]

    antinodes = set()

    for points in M.values():
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                for a1, a2 in gen_antinode(points[i], points[j]):
                    if 0 <= a1 < h and 0 <= a2 < w:
                        antinodes.add((a1, a2))

    return len(antinodes)


def part2(inp: list[str]) -> int:
    h, w, M = parse_input(inp)

    def gen_antinode(p1: tuple[int], p2: tuple[int]) -> list[tuple[int]]:

        def one_direction(p3: tuple[int], p4: tuple[int]) -> list[tuple[int]]:
            partial = []
            x1, y1 = p3
            x2, y2 = p4
            k = 0
            while True:
                xa = x1 + k * (x1 - x2)
                ya = y1 + k * (y1 - y2)
                if 0 <= xa < h and 0 <= ya < w:
                    partial.append((xa, ya))
                else:
                    return partial

                k += 1

        antis = one_direction(p1, p2)
        antis.extend(one_direction(p2, p1))

        return antis

    antinodes = set()

    for points in M.values():
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                antinodes.update(gen_antinode(points[i], points[j]))

    return len(antinodes)


if __name__ == "__main__":
    input_str = read_input_file("C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day8\\input.txt")
    print(part1(input_str))
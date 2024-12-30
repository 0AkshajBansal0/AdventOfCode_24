from math import lcm
from re import findall

def q2(lines):
    lines = " ".join(lines)
    a = [(int(x), int(y)) for x, y in findall(r"Button A: X\+(\d+), Y\+(\d+)", lines)]
    b = [(int(x), int(y)) for x, y in findall(r"Button B: X\+(\d+), Y\+(\d+)", lines)]
    p = [
        (int(x) + 10_000_000_000_000, int(y) + 10_000_000_000_000)
        for x, y in findall(r"Prize: X=(\d+), Y=(\d+)", lines)
    ]

    tokens = 0
    for (ax, ay), (bx, by), (px, py) in zip(a, b, p):
        m = lcm(ax, ay)

        cx = m // ax
        ax *= cx
        bx *= cx
        px *= cx

        cy = m // ay
        ay *= cy
        by *= cy
        py *= cy

        assert ax == ay

        b = (px - py) // (bx - by)
        a = (px - bx * b) // ax

        if a * ax + b * bx == px and a * ay + b * by == py:
            tokens += 3 * a + b
    return tokens

if __name__ == "__main__":
    with open("C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day13\\input.txt", "r") as file:
        lines = file.readlines()
    print("Part 2:", q2(lines))
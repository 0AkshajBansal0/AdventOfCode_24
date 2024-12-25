from collections import deque, defaultdict

def q2():
    with open("C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day11\\input.txt", "r") as file:
        lines = file.readlines()
    stones = {int(s): 1 for s in lines[0].split()}
    for _ in range(75):
        newstones = defaultdict(int)
        for stone, count in stones.items():
            ss = str(stone)
            if stone == 0:
                newstones[1] += count
            elif len(ss) % 2 != 0:
                newstones[stone * 2024] += count
            else:
                newstones[int(ss[:len(ss)//2])] += count
                newstones[int(ss[len(ss)//2:])] += count
        stones = newstones
    return sum(stones.values())

if __name__ == "__main__":
    print(q2())
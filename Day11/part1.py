from collections import deque, defaultdict

def q1():
    with open("C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day11\\input.txt", "r") as file:
        lines = file.readlines()
    stones = [int(s) for s in lines[0].split()]
    for _ in range(25):
        newstones = []
        for i, s in enumerate(stones):
            ss = str(s)
            if s == 0:
                stones[i] = 1
            elif len(ss) % 2 != 0:
                stones[i] *= 2024
            else:
                stones[i] = int(ss[:len(ss)//2])
                newstones.append((i+1+len(newstones), int(ss[len(ss)//2:])))
        for p, s in newstones:
            stones.insert(p, s)
    return len(stones)

if __name__ == "__main__":
    print(q1())
import time
from typing import Literal
from collections import deque

def common(input_path: str):
    with open(input_path, "r") as file:
        data = file.read().strip()
        data = list(map(int, list(data)))

        decompressed = []
        for idx, n in enumerate(data):
            if idx % 2 == 0:
                decompressed.extend([idx // 2] * n)
            else:
                decompressed.extend([-1] * n)

    return decompressed

def part_one(input_path: str):
    disk_map = common(input_path)

    free_space = deque([idx for idx, n in enumerate(disk_map) if n == -1])
    queue = deque(disk_map)
    while queue:
        v = queue.pop()

        if v == -1:
            continue

        pop_idx = len(queue)
        slot_idx = free_space.popleft()

        disk_map[pop_idx], disk_map[slot_idx] = disk_map[slot_idx], disk_map[pop_idx]

        # Check for free space limit of 10
        if all(val == -1 for val in disk_map[slot_idx + 1:slot_idx + 10]):
            break

    checksum = 0
    no_slots = list(filter(lambda x: x != -1, disk_map))
    for idx, n in enumerate(no_slots):
        checksum += idx * n

    return checksum


if __name__ == "__main__":
    input_file = "C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day9\\input.txt"

    start_one = time.perf_counter()
    result_one = part_one(input_file)
    end_one = time.perf_counter()
    print(result_one)
import os
from collections import *
from functools import *
from itertools import *
from math import *

def main_part_2(inp: list[str]) -> int:
    if len(inp[0]) % 2 == 0:
        inp[0] = inp[0][:-1]

    files: list[tuple[int, int]] = []
    holes: list[int] = []

    for index, size in enumerate(map(int, inp[0])):
        if index % 2 == 0:
            files.append((index // 2, size))
        else:
            holes.append(size)
            

    for file_index in range(len(files) - 1, -1, -1):
        file_location_index, file_size = \
            next(((f_location, f_size) 
                  for f_location, (f_index, f_size)
                  in enumerate(files)
                  if f_index == file_index))

        
        hole_location_index, hole_size = \
            next(((h_location, h_size)
                  for h_location, h_size
                  in enumerate(holes[:file_location_index])
                  if h_size >= file_size), (-1, -1))

        if hole_size == -1:
            continue

        # remove file
        files.pop(file_location_index)
        remvoed_hole_size = holes.pop(file_location_index - 1)

        if file_location_index != len(files):
            holes[file_location_index - 1] += remvoed_hole_size + file_size

        # put file back
        files.insert(hole_location_index + 1, (file_index, file_size))
        holes[hole_location_index] -= file_size
        holes.insert(hole_location_index, 0)


    index = 0
    total = 0
    for file_data, hole_size in zip_longest(files, holes):
        if file_data:
            file_index, file_size = file_data
            total += file_index * (index * file_size + file_size * (file_size - 1) // 2)
            index += file_size
        
        if hole_size:
            index += hole_size

    return total

def main() -> None:
    test_input = """2333133121414131402"""
    test_input_parsed = test_input.splitlines()
    test_output_part_2_expected = 2858

    file_location = os.path.dirname(os.path.realpath(__file__))
    file_location = file_location + "/input.txt"
    with open(file_location, "r") as file:
        input_file = file.read().splitlines()

    test_output_part_2 = main_part_2(test_input_parsed)

    if test_output_part_2_expected != test_output_part_2:
        print(f"Part 2 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_2_expected}")
        print(f"Got: {test_output_part_2}")
        print()

    if test_output_part_2_expected == test_output_part_2:
        print(main_part_2(input_file))


if __name__ == "__main__":
    main()
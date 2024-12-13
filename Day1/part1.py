def total_distance(file_path):
    left_list = []
    right_list = []

    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)

    left_list.sort()
    right_list.sort()

    total = 0
    for left, right in zip(left_list, right_list):
        total += abs(left - right)

    return total

file_path = "C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day1\\input.txt"
result = total_distance(file_path)
print(result)

def similarity_score(file_path):
    left_list = []
    right_list = []

    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)

    right_count = {}                      #right_count = {3: 4, 4: 1, 5: 1, 9: 1}
    for num in right_list:
        if num in right_count:
            right_count[num] += 1
        else:
            right_count[num] = 1

    score = 0
    for number in left_list:
        frequency = right_count.get(number, 0)
        score += number * frequency

    return score

file_path = "C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day1\\input.txt"
result = similarity_score(file_path)
print(result)
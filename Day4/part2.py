def count_xmas_part2(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file]

    rows = len(grid)
    cols = len(grid[0])
    word = "MAS"
    total_count = 0
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            left_diag = grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1]
            right_diag = grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1]
            if (left_diag == word or left_diag[::-1] == word) and \
               (right_diag == word or right_diag[::-1] == word):
                total_count += 1
    return total_count

file_path = "C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day4\\input.txt"
result = count_xmas_part2(file_path)
print(result)
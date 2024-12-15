def count_xmas(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file]
    
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_len = len(word)
    total_count = 0

    # Check horizontally
    for row in grid:
        total_count += row.count(word)
        total_count += row[::-1].count(word)

    # Check vertically
    for col in range(cols):
        column_str = ''.join(grid[row][col] for row in range(rows))
        total_count += column_str.count(word)
        total_count += column_str[::-1].count(word)

    # Check diagonals
    for start in range(-rows + 1, cols):
        diag1 = ''.join(grid[i][i - start] for i in range(max(0, start), min(rows, cols + start)) if 0 <= i - start < cols)
        total_count += diag1.count(word)  # Top-left to bottom-right
        total_count += diag1[::-1].count(word)  # Bottom-right to top-left

    for start in range(rows + cols - 1):
        diag2 = ''.join(grid[i][start - i] for i in range(max(0, start - cols + 1), min(rows, start + 1)) if 0 <= start - i < cols)
        total_count += diag2.count(word)  # Top-right to bottom-left
        total_count += diag2[::-1].count(word)  # Bottom-left to top-right

    return total_count

file_path = "C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day4\\input.txt"
result = count_xmas(file_path)
print(result)
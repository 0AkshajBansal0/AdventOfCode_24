def move_guard(map, start_row, start_col, direction):
    # Direction mappings: (row_offset, col_offset)
    directions = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    # Set the initial position
    row, col = start_row, start_col
    visited = set()  # To track the distinct positions visited
    
    while 0 <= row < len(map) and 0 <= col < len(map[0]):
        # Add current position to visited set
        visited.add((row, col))
        
        # Check the next space in the current direction
        dr, dc = directions[direction]
        new_row, new_col = row + dr, col + dc
        
        # Exit condition if the new position is outside the map
        if not (0 <= new_row < len(map) and 0 <= new_col < len(map[0])):
            break  # The guard is leaving the area
        
        if map[new_row][new_col] != '#':
            # Move to the next position if it's not an obstacle
            row, col = new_row, new_col
        else:
            # Turn right 90 degrees if there is an obstacle
            direction = turn_right[direction]
    
    return len(visited)

# Read the map from the input file
def read_input(file_path):
    with open(file_path, 'r') as file:
        map = [list(line.strip()) for line in file.readlines()]
    
    # Find the starting position of the guard
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] in '^v<>':
                start_row, start_col, direction = r, c, map[r][c]
                map[r][c] = '.'  # Replace the guard with empty space once they start moving
                return map, start_row, start_col, direction
    
    return map, -1, -1, ''  # Return an empty case if no starting position is found

def solve(file_path):
    map, start_row, start_col, direction = read_input(file_path)
    if start_row == -1 or start_col == -1:
        return 0  # No valid start position
    
    return move_guard(map, start_row, start_col, direction)

file_path = "C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day6\\input.txt"
result = solve(file_path)
print(result)
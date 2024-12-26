# Directions for 4 possible neighbors (up, down, left, right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_bounds(r, c, rows, cols):
    """Check if the cell is within the bounds of the grid."""
    return 0 <= r < rows and 0 <= c < cols

def flood_fill(grid, r, c, visited, plant_type):
    """Flood fill to find all plots in the same region."""
    stack = [(r, c)]
    region = []
    while stack:
        x, y = stack.pop()
        if (x, y) not in visited:
            visited.add((x, y))
            region.append((x, y))
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if in_bounds(nx, ny, len(grid), len(grid[0])) and grid[nx][ny] == plant_type and (nx, ny) not in visited:
                    stack.append((nx, ny))
    return region

def calculate_perimeter(grid, region):
    """Calculate the perimeter of a given region."""
    perimeter = 0
    for r, c in region:
        # Check each of the 4 possible neighbors
        for dx, dy in DIRECTIONS:
            nr, nc = r + dx, c + dy
            # If the neighbor is out of bounds or a different plant type, it contributes to the perimeter
            if not in_bounds(nr, nc, len(grid), len(grid[0])) or grid[nr][nc] != grid[r][c]:
                perimeter += 1
    return perimeter

def total_fence_cost(grid):
    """Calculate the total cost of the fence around all regions."""
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    total_cost = 0

    # Traverse the grid to find all regions
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                plant_type = grid[r][c]
                region = flood_fill(grid, r, c, visited, plant_type)
                area = len(region)
                perimeter = calculate_perimeter(grid, region)
                total_cost += area * perimeter

    return total_cost

file_path = "C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day12\\input.txt"
with open(file_path, 'r') as file:
    grid = [line.strip() for line in file.readlines()]

result = total_fence_cost(grid)
print(result)
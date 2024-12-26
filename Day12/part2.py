class Plot:
    def exposed_sides(self):
        return 4 - len(self.neighbours)

    def __init__(self, plant_type):
        self.plant_type = plant_type
        self.neighbours = {}

    def __str__(self):
        return self.plant_type

    def add_neighbour(self, direction, other_node):
        if self.plant_type == other_node.plant_type:
            self.neighbours[direction] = other_node

    def _find_region(self, region):
        if self not in region:
            region.add(self)
            for neighbour in self.neighbours.values():
                neighbour._find_region(region)

        return region

    def get_region(self):
        return Region(self._find_region(set()))


class Region:
    def __init__(self, node_set):
        self.node_set = node_set

    def perimeter(self):
        return sum(plot.exposed_sides() for plot in self.node_set)

    def area(self):
        return len(self.node_set)

    def count_sides_from(self, start_node, direction, visited):
        if direction in start_node.neighbours:
            return 0

        if (start_node, direction) in visited:
            return 0

        normal = direction
        clockwise_direction = {'u': 'r', 'r': 'd', 'd': 'l', 'l': 'u'}
        travel = clockwise_direction[normal]
        opposite_direction = {'u': 'd', 'd': 'u', 'l': 'r', 'r': 'l'}

        node = start_node
        back_at_start = False
        sides = 0
        while not back_at_start:
            visited.add((node, normal))
            if travel in node.neighbours:
                travel_node = node.neighbours[travel]
                if normal in travel_node.neighbours:
                    node = travel_node.neighbours[normal]
                    sides += 1
                    (normal, travel) = opposite_direction[travel], normal
                else:
                    node = travel_node
            else:
                sides += 1
                (normal, travel) = travel, opposite_direction[normal]

            back_at_start = (node == start_node) and normal == direction

        return sides

    def side_count(self):
        visited = set()
        total_sides = 0
        for node in self.node_set:
            for direction in "udlr":
                total_sides += self.count_sides_from(node, direction, visited)

        return total_sides


class Puzzle:
    def __init__(self, lines):
        self.matrix = []
        prev_row = None
        for line in lines:
            row = []
            left_plot = None
            for (j, v) in enumerate(line):
                plot = Plot(v)
                if left_plot is not None:
                    plot.add_neighbour('l', left_plot)
                    left_plot.add_neighbour('r', plot)
                if prev_row is not None:
                    up_plot = prev_row[j]
                    plot.add_neighbour('u', up_plot)
                    up_plot.add_neighbour('d', plot)
                left_plot = plot
                row.append(plot)
            self.matrix.append(row)
            prev_row = row

    def __str__(self):
        return "\n".join("".join(str(p) for p in line) for line in self.matrix)

    def get_regions(self):
        visited_nodes = set()
        regions = set()
        for row in self.matrix:
            for plot in row:
                if plot in visited_nodes:
                    continue
                region = plot.get_region()
                regions.add(region)
                visited_nodes = visited_nodes.union(region.node_set)

        return regions

    def bulk_discount(self):
        return sum(region.area() * region.side_count() for region in self.get_regions())


def accept_input(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return Puzzle([line.strip() for line in lines])


def part2(puzzle):
    return puzzle.bulk_discount()


def main():
    puzzle = accept_input("C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day12\\input.txt")
    print(f"Part 2: {part2(puzzle)}")

main()
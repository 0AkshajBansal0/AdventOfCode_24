class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

def FindAllPoints(map, symbol):
    points = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == symbol:
                points.append(Point(x, y))
    return points

def IsInMap(map, point):
    return point.y >= 0 and point.y < len(map) and point.x >= 0 and point.x < len(map[point.y])

def NextPoints(map, point, level):
    nextPoints = set()
    p = MoveUp(point)
    if IsInMap(map, p) and map[p.y][p.x] == level:
        nextPoints.add(p)
    p = MoveDown(point)
    if IsInMap(map, p) and map[p.y][p.x] == level:
        nextPoints.add(p)
    p = MoveLeft(point)
    if IsInMap(map, p) and map[p.y][p.x] == level:
        nextPoints.add(p)
    p = MoveRight(point)
    if IsInMap(map, p) and map[p.y][p.x] == level:
        nextPoints.add(p)
    return nextPoints

def MoveUp(point):
    return Point(point.x, point.y - 1)

def MoveDown(point):
    return Point(point.x, point.y + 1)

def MoveLeft(point):
    return Point(point.x - 1, point.y)

def MoveRight(point):
    return Point(point.x + 1, point.y)

def ReadAllMap(f):
    map = []
    for line in f:
        map.append([int(x) for x in list(line.strip())])
    return map

def Score(map, point):
    level = 0
    nextPositions = set()
    currentPositions = set()
    currentPositions.add(point)
    while len(currentPositions) > 0 and level < 9:
        level += 1
        for position in currentPositions:
            nextPositions = nextPositions.union(
                NextPoints(map, position, level))
        currentPositions = nextPositions
        nextPositions = set()
    if level == 9:
        return len(currentPositions)
    return 0

def Rating(map, point):
    level = 0
    currentPaths = []
    currentPaths.append([point])
    while len(currentPaths) > 0 and level < 9:
        level += 1
        newPaths = []
        for currentPath in currentPaths:
            lastPosition = currentPath[-1]
            if map[lastPosition.y][lastPosition.x] < level - 1:
                continue
            for point in NextPoints(map, lastPosition, level):
                newPaths.append(currentPath + [point])
        currentPaths = newPaths
    if level == 9:
        return len(currentPaths)
    return 0

def P1(map):
    startingPositions = FindAllPoints(map, 0)
    scores = [Score(map, point) for point in startingPositions]
    return sum(scores)

with open("C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day10\\input.txt", "r") as f:
    map = ReadAllMap(f)

print(P1(map))
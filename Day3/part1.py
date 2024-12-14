import re

def process_memory(file_path):
    total = 0
    
    with open(file_path, 'r') as file:
        corrupted_memory = file.read()
    
    #Regular expression to match correct mul(X,Y)
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, corrupted_memory)
    
    for x, y in matches:
        total += int(x) * int(y)
    
    return total

file_path = "C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day3\\input.txt"
result = process_memory(file_path)
print(result)

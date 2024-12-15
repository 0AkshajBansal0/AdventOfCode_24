import re

def process_memory(file_path):
    total = 0
    mul_enabled = True

    with open(file_path, 'r') as file:
        corrupted_memory = file.read()
    
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    condition_pattern = r"(do\(\)|don't\(\))"

    instructions = re.findall(f"{mul_pattern}|{condition_pattern}", corrupted_memory)

    for instr in instructions:
        #Match for do() or don't()
        if instr[2]:
            if instr[2] == "do()":
                mul_enabled = True
            elif instr[2] == "don't()":
                mul_enabled = False
        #Match for mul(X, Y) and mul is enabled
        elif mul_enabled:
            x, y = int(instr[0]), int(instr[1])
            total += x * y
    
    return total

file_path = "C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day3\\input.txt"
result = process_memory(file_path)
print(result)
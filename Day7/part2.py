import itertools

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '||':
            result = int(str(result) + str(numbers[i + 1]))  # Concatenate numbers as a string
    return result

def solve(file_path):
    total_sum = 0
    
    # Read input
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        test_value_str, numbers_str = line.split(':')
        test_value = int(test_value_str.strip())
        numbers = list(map(int, numbers_str.split()))
        
        # Limit operator combinations to reduce redundancy
        operator_combinations = itertools.product(['+', '*', '||'], repeat=len(numbers) - 1)
        
        # Try to break early once a valid solution is found
        for operators in operator_combinations:
            result = evaluate_expression(numbers, operators)
            if result == test_value:
                total_sum += test_value
                break  # Exit loop once valid result is found
    
    return total_sum

file_path = "C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day7\\input.txt"
result = solve(file_path)
print(result)
import itertools

def evaluate_expression(numbers, operators):
    # Evaluate the expression left to right with given operators
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
    return result

def solve(file_path):
    total_sum = 0
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        test_value_str, numbers_str = line.split(':')
        test_value = int(test_value_str.strip())
        numbers = list(map(int, numbers_str.split()))
        
        # Generate all possible operator combinations (+ and *)
        operator_combinations = itertools.product(['+', '*'], repeat=len(numbers) - 1)
        
        # Check each combination of operators
        for operators in operator_combinations:
            if evaluate_expression(numbers, operators) == test_value:
                total_sum += test_value
                break  # No need to check further combinations for this equation
    
    return total_sum

file_path = "C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day7\\input.txt"
result = solve(file_path)
print(result)
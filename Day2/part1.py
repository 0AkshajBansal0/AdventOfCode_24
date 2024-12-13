def is_safe_report(report):
    
    #for checking difference
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i+1])
        if diff < 1 or diff > 3:
            return False
        
    #for checking increasing or decreasing
    increasing = decreasing = True
    for i in range(len(report) - 1):
        if report[i] < report[i + 1]:
            decreasing = False
        elif report[i] > report[i + 1]:
            increasing = False

    return increasing or decreasing


def count_safe_reports(file_path):
    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.strip().split()))    
            if is_safe_report(report):
                safe_count += 1
    return safe_count

file_path = "C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day2\\input.txt"
result = count_safe_reports(file_path)
print(result)

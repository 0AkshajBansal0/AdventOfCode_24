def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().split("\n")
    
    # Separate rules and updates
    rules = []
    updates = []
    in_rules = True
    for line in lines:
        line = line.strip()
        if not line:  #Skip blank lines
            continue
        if '|' in line:
            try:
                x, y = map(int, line.split('|'))
                rules.append((x, y))
            except ValueError:
                continue  #Skip malformed rules
        else:
            try:
                update = list(map(int, line.split(',')))
                updates.append(update)
            except ValueError:
                continue  #Skip malformed updates
    
    return rules, updates

def is_update_valid(update, rules):
    pos = {page: i for i, page in enumerate(update)}
    
    # Check each rule
    for x, y in rules:
        if x in pos and y in pos:  #Rule applies to this update
            if pos[x] > pos[y]:  #Rule is violated
                return False
    return True

def sum_middle_pages(file_path):
    rules, updates = parse_input(file_path)
    total = 0

    for update in updates:
        if is_update_valid(update, rules):
            middle_idx = len(update) // 2
            total += update[middle_idx]
    
    return total

file_path = "C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day5\\input.txt"
result = sum_middle_pages(file_path)
print(result)

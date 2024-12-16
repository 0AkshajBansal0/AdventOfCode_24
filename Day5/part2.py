def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().split("\n")
    
    rules = []
    updates = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if '|' in line:
            x, y = map(int, line.split('|'))
            rules.append((x, y))
        else:
            updates.append(list(map(int, line.split(','))))
    
    return rules, updates

def is_update_valid(update, rules):
    pos = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in pos and y in pos:
            if pos[x] > pos[y]:
                return False
    return True

def reorder_update(update, rules):
    # Repeatedly apply rules until the order stabilizes
    while True:
        changed = False
        for x, y in rules:
            if x in update and y in update:
                xi, yi = update.index(x), update.index(y)
                if xi > yi:  #Swap to ensure x comes before y
                    update[xi], update[yi] = update[yi], update[xi]
                    changed = True
        if not changed:
            break
    return update

def sum_incorrect_middle_pages(file_path):
    rules, updates = parse_input(file_path)
    total = 0

    for update in updates:
        if not is_update_valid(update, rules):
            corrected_update = reorder_update(update, rules)
            middle_idx = len(corrected_update) // 2
            total += corrected_update[middle_idx]
    
    return total

file_path = "C:\\Users\\Akshaj Bansal\\OneDrive\\Desktop\\VS_CODE\\AdventOfCode_24\\Day5\\input.txt"
result = sum_incorrect_middle_pages(file_path)
print(result)

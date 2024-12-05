def check_correctness(line):
    is_not_in_rules = False
    for i, num in enumerate(line):
        if num in rules_dict:
            if is_not_in_rules:
                return False
            if not (all(element in rules_dict[line[i]] for element in line[i + 1:])):
                return False
    return True

def fill_rules(input_file):
    rules = input_file.split("\n")
    rules_dict = {}
    for first, second in [map(int, j.split('|')) for j in rules]:
        rules_dict.setdefault(first, []).append(second)
    return rules_dict


def sort_line(line, rules_dict):
    dependencies = {num: set(rules_dict[num]) & set(line) if num in rules_dict else [] for num in line}

    sorted_line = []
    while dependencies:
        independent = [num for num, deps in dependencies.items() if not deps]
        sorted_line.extend(independent)

        for num in independent:
            del dependencies[num]
            for dep in dependencies.values():
                dep.discard(num)
    return sorted_line


with open('Day5.txt') as file:
    rules_section, data_section = file.read().split('\n\n')
    rules_dict = fill_rules(rules_section)
    data = [list(map(int, i.split(','))) for i in data_section.split("\n")]

    result = 0
    for line in data:
        if not(check_correctness(line)):
            result += sort_line(line, rules_dict)[len(line) // 2]
    print(result)

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

with open('Day5.txt') as file:
    rules_section, data_section = file.read().split('\n\n')
    rules_dict = fill_rules(rules_section)
    data = [list(map(int, i.split(','))) for i in data_section.split("\n")]

    result = sum([line[len(line) // 2] for line in data if check_correctness(line)])
    print(result)
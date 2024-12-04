count = 0

with open("Day2.txt") as file:
    reports = [list(map(int, line.split())) for line in file.readlines()]

    def is_safe(report):
        diff = [report[i + 1] - report[i] for i in range(len(report) - 1)]
        return ((all(n > 0 for n in diff)) or (all(n < 0 for n in diff))) and (all(1 <= abs(n) <= 3 for n in diff))

    for report in reports:
        if is_safe(report):
            count += 1

    print(count)
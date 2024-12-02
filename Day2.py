reports = []
count = 0
a = input()

while len(a) != 0:
    reports.append(list(map(int, a.split())))
    a = input()

def is_safe(report):
    diff = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    return ((all(n > 0 for n in diff)) or (all(n < 0 for n in diff))) and (all(1 <= abs(n) <= 3 for n in diff))

# 1.1)
# for report in reports:
#     if is_safe(report):
#         count += 1

# 1.2)
for report in reports:
    if is_safe(report):
        count += 1
    else:
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if is_safe(modified_report):
                count += 1
                break

print(count)
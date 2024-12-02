first_list = []
second_list = []
a = input()

while len(a) != 0:
    data = a.split()
    first_list.append(int(data[0]))
    second_list.append(int(data[1]))
    a = input()

first_list = sorted(first_list)
second_list = sorted(second_list)

# 1.1)
# result = [abs(first_list[i] - second_list[i]) for i in range(len(first_list))]
# 1.2)
result = [(first_list[i] * second_list.count(first_list[i])) for i in range(len(first_list))]
print(sum(result))
first_list = []
second_list = []

with open("Day1.txt") as file:
    for line in file.readlines():
        data = line.split()
        first_list.append(int(data[0]))
        second_list.append(int(data[1]))
        line = file.readline()

    first_list = sorted(first_list)
    second_list = sorted(second_list)

    result = [(first_list[i] * second_list.count(first_list[i])) for i in range(len(first_list))]
    print(sum(result))
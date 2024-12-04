X_MAS = ["MAS", 'SAM']

with open("Day4.txt") as file:
    pattern = r"MAS|SAM"
    data = [line.strip() for line in file.readlines()]
    count = 0

    for i in range(len(data) - 2):
        for j in range(len(data[0]) - 2):
            first_diagonal = data[i][j] + data[i + 1][j + 1] + data[i + 2][j + 2]
            second_diagonal = data[i][j + 2] + data[i + 1][j + 1] + data[i + 2][j]
            if first_diagonal in X_MAS and second_diagonal in X_MAS:
                count+=1
    print(count)




import re

def find_overlapping_matches(text, pattern):
    matches = []
    start = 0
    while start < len(text):
        match = re.search(pattern, text[start:])
        if not match:
            break
        matches.append(match.group())
        start += match.start() + 1
    return matches

def extract_diagonals(matrix, direction="right"):

    first_row = matrix[0]
    diagonals = []

    for i in range(len(first_row)):
        diagonal = []
        for row_idx, row in enumerate(matrix):
            if direction == "right":
                char_index = i + row_idx
            elif direction == "left":
                char_index = i - row_idx

            if 0 <= char_index < len(row):
                diagonal.append(row[char_index])
        diagonals.append("".join(diagonal))

    for row_idx, row in enumerate(matrix[1:], start=1):
        for i in (0, len(row) - 1):
            diagonal = []
            for next_row_idx, next_row in enumerate(matrix[row_idx:]):
                if direction == "right":
                    char_index = i + next_row_idx
                elif direction == "left":
                    char_index = i - next_row_idx

                if 0 <= char_index < len(next_row):
                    diagonal.append(next_row[char_index])
            diagonals.append("".join(diagonal))

    return diagonals


with open("Day4.txt") as file:
    pattern = r"XMAS|SAMX"
    data = [line.strip() for line in file.readlines()]
    column_count = 0
    lines = [find_overlapping_matches(line, pattern) for line in data if find_overlapping_matches(line, pattern)]
    line_count = sum([len(line) for line in lines])

    for i in range(len(data)):
        columns = "".join([x[i] for x in data])
        columns = find_overlapping_matches(columns, pattern)
        column_count += len(columns)

    left_diagonals = extract_diagonals(data, direction="left")
    left_diagonals = [find_overlapping_matches(diagonal, pattern) for diagonal in left_diagonals if find_overlapping_matches(diagonal, pattern)]

    right_diagonals = extract_diagonals(data)
    right_diagonals = [find_overlapping_matches(diagonal, pattern) for diagonal in right_diagonals if find_overlapping_matches(diagonal, pattern)]

    left_diagonals_count = sum([len(diagonal) for diagonal in left_diagonals])
    right_diagonals_count = sum([len(diagonal) for diagonal in right_diagonals])
    print(line_count + column_count + left_diagonals_count + right_diagonals_count)

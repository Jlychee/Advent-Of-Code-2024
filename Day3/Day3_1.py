import re

pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"

with open("Day3.txt") as file:
    input_text = file.read()

all_input_data = [int(i[0])*int(i[1]) for i in re.findall(pattern, input_text)]

print(sum(all_input_data))
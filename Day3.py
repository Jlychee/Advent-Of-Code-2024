import re

pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
dont_pattern = r"(?<=don't\(\))([\s\S]*?)(?=do\(\)|$)"

with open("Day3_1_data.txt") as file:
    input_text = file.read()

all_input_data = [int(i[0])*int(i[1]) for i in re.findall(pattern, input_text)]
match = re.findall(dont_pattern, input_text)
all_dont_input_data = [int(i[0])*int(i[1]) for i in re.findall(pattern, "".join(match))]

print(sum(all_input_data) - sum(all_dont_input_data))
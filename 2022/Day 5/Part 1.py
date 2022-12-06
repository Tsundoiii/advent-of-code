crates, instructions = open("input.txt").read().split("\n\n")

instructions = instructions.splitlines()

crate_input_lines = []

for line in crates.splitlines()[:-1]:
    line_array = []
    for i in range(0, 36, 4):
        line_array.append(line[i:i + 4])
    crate_input_lines.append(line_array)

for line in crate_input_lines:
    print(line)

crate_array = []

for column in range(8):
    column_array = []
    for row in range(8):
        print(f"[{row}][{column}]")
        print(crate_input_lines[row][column])
        column_array.append(crate_input_lines[row][column])
    crate_array.append(column_array)

for ca in crate_array:
    print(ca)

def print_crates(crates: list[list[str]]):
    pass

#print(crates)
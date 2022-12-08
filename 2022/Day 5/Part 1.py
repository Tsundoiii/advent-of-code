crates, instructions = open("input.txt").read().split("\n\n")

instructions = instructions.splitlines()

instructions = [{"move": int(instruction.split(" ")[1]), "from": int(instruction.split(" ")[3]) - 1, "to": int(instruction.split(" ")[5]) - 1} for instruction in instructions]

crate_input_lines = []

for line in crates.splitlines()[:-1]:
    line_array = []
    for i in range(0, 36, 4):
        line_array.append(line[i:i + 4])
    crate_input_lines.append(line_array)

crate_array = []

for column in range(9):
    column_array = []
    for row in range(8):
        column_array.append(crate_input_lines[row][column])
    crate_array.append(column_array)

crate_array = [[c for c in crate if c != '    ' and c != '   '] for crate in crate_array]

for i in instructions:
    for j in range(i["move"]):
        crate_array[i["to"]].insert(0, crate_array[i["from"]][0])
        crate_array[i["from"]].pop(0)

for ca in crate_array:
    print(ca[0])
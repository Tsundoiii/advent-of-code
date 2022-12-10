input = open("input.txt").readlines()

X = 1

cycle = 0

values = {}

sum = 0

for instruction in input:
    if instruction.startswith("noop"):
        cycle += 1
    else:
        cycle += 2
        X += int(instruction.split()[1])
        values.update({cycle: X})

for i in range(20, 221, 40):
    for j in range(i - 1, 0, -1):
        if j in values.keys():
            sum += values[j] * i
            break

print(sum)
input = open("input.txt").readlines()

input = [line.split("\t") for line in input]

checksum = 0

for line in input:
    input[input.index(line)] = [int(number) for number in line]

for line in input:
    checksum += max(line) - min(line)

print(f"{checksum = }")
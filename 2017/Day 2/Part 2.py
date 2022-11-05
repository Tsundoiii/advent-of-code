input = open("input.txt").readlines()

input = [line.split("\t") for line in input]

result = 0

for line in input:
    input[input.index(line)] = [int(number) for number in line]

def find_nums(line):
    for num in line:
        for num2 in line:
            if num % num2 == 0 and num != num2:
                return num // num2

for line in input:
    result += find_nums(line)

print(f"{result = }")
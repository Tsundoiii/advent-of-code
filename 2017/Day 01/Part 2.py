input = open("input.txt").read().rstrip()

sum = 0

for i in range(len(input) - 1):
    if int(input[i]) == int(input[(i + len(input) // 2) % len(input)]):
        sum += int(input[i])

print(sum)
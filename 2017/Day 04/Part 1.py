input = [line.split() for line in open("input.txt").readlines()]

valid = 0

for line in input:
    for word in line:
        if line.count(word) > 1:
            break
    else:
        valid += 1

print(f"{valid = }")
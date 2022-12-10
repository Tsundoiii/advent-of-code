positionFile = open('input.txt')
f = positionFile.readlines()

horizontal = 0
depth = 0
aim = 0

for x in f:
    a = x.split()
    if a[0] == "forward":
        horizontal += int(a[1])
        depth += aim * int(a[1])
    elif a[0] == "down":
        aim += int(a[1])
    elif a[0] == "up":
        aim -= int(a[1])

total = horizontal * depth

print(f"The net horizontal value is {horizontal}")
print(f"The net depth is {depth}")
print(f"The net aim is {aim}")
print(f"The net total is {total}")
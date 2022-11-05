input = [side.split() for side in open("input.txt").readlines()]

for sides in input:
    for side in sides:
        sides[sides.index(side)] = int(side)

count = 0

for sides in input:
    if sides[0] + sides[1] > sides[2]:
        print(f"{sides}: {sides[0] + sides[1]}")
        count += 1

print(f"Count: {count}")
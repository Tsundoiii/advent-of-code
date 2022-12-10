input = [[[int(z) for z in y.split("-")] for y in x.split(",")] for x in open("input.txt").readlines()]

total = 0

for i in input:
    if (i[0][0] >= i[1][0] and i[0][1] <= i[1][1]) or (i[1][0] >= i[0][0] and i[1][1] <= i[0][1]):
        total += 1

print(total)
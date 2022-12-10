input = [[[int(z) for z in y.split("-")] for y in x.split(",")] for x in open("input.txt").readlines()]

total = 0

for i in input:
    if i[1][0] < i[0][0]:
        new = [i[1], i[0]]
    else:
        new = i

    if new[1][0] <= new[0][1]:
        total += 1

print(total)
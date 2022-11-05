input = [dimension.split("x") for dimension in open("input.txt").readlines()]

calculatePaper = lambda l, w, h : (2 * l * w) + (2 * w * h) + (2 * h * l)
smallestSide = lambda l, w, h : min(l * w, w * h, l * h)

total = 0

for dimension in input:
    total += (calculatePaper(int(dimension[0]), int(dimension[1]), int(dimension[2])) + smallestSide(int(dimension[0]), int(dimension[1]), int(dimension[2])))

print(f"Total: {total}")
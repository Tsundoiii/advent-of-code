input = open("input.txt").readlines()

X = 1
cycle = 0
pixels = [' '] * 40 * 6

for instruction in input:
    sprite = list(range(X - 1, X + 2))
    if cycle % 40 in sprite:
        pixels[cycle] = '#'

    if instruction.startswith("noop"):
        cycle += 1
    else:
        if cycle % 40 in sprite:
            pixels[cycle] = '#'
        cycle += 1
        if cycle % 40 in sprite:
            pixels[cycle] = '#'
        cycle += 1
        X += int(instruction.split()[1])

for i in range(0, 240, 40):
    print(''.join(pixels[i:i + 40]))
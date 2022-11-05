depthsFile = open('input.txt')
f = depthsFile.readlines()
depths = [int(x) for x in f]

lastDepth = depths[0]
increase = 0
decrease = 0

for x in depths:
    if x > lastDepth:
        increase += 1
        lastDepth = x
    elif x < lastDepth:
        decrease += 1
        lastDepth = x

print(f"It has increased {increase} times")
print(f"It has decreased {decrease} times")
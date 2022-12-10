depthsFile = open('input.txt')
f = depthsFile.readlines()
depths = [int(x) for x in f]

lastDepth = depths[0]
increase = 0
decrease = 0

windowSums = []

aIndex = 0
bIndex = 3

for x in depths:
    windowSum = sum(depths[aIndex:bIndex])
    windowSums.append(windowSum)
    aIndex += 1
    bIndex += 1

lastWindowSum = windowSums[0]

for x in windowSums:
    if x > lastWindowSum:
        increase += 1
        lastWindowSum = x
    elif x < lastWindowSum:
        decrease += 1
        lastWindowSum = x

print(f"It has increased {increase} times")
print(f"It has decreased {decrease} times")
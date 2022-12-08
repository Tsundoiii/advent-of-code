input = open("input.txt").read()

visited = {
    (0, 0): 1
}
last = [0, 0]

for move in input:
    house = last
    match move:
        case "^":
            house[1] += 1
        case "v":
            house[1] -= 1
        case ">":
            house[0] += 1
        case "<":
            house[0] -= 1
    if (house[0], house[1]) in visited.keys():
        visited[(house[0], house[1])] += 1
    else:
        visited.update({
            (house[0], house[1]): 1
        })

print(len(visited))
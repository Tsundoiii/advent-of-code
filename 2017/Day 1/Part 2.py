input = open("input.txt").read().split(", ")
test = "R8, R4, R4, R8".split(", ")
test = [[i[0], int(i[1:])] for i in test]
direction = 0

x = 0
y = 0

input = [[i[0], int(i[1:])] for i in input]
points = [[0, 0]]

for j in input:
    print(j)
    match j[0]:
        case 'R':
            direction += 90
        case 'L':
            direction -= 90
    match direction % 360:
        case 0 | 360:
            for k in range(abs(y - j[1])):
                y += 1
                points.append([x, y])
                print([x, y])
        case 90 | -270:
            for k in range(abs(x - j[1])):
                x += 1
                points.append([x, y])
                print([x, y])
        case 180 | -180:
            for k in range(abs(y - j[1])):
                y -= 1
                points.append([x, y])
                print([x, y])
        case 270 | -90:
            for k in range(abs(x - j[1])):
                x -= 1
                points.append([x, y])
                print([x, y])

new_points = []
for point in points:
    if point in new_points:
        print(point)
        print(abs(0 - point[0]) + abs(0 - point[1]))
        break
    else:
        new_points.append(point)
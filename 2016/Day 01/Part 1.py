input = open("input.txt").read().split(", ")


direction = 0

x = 0
y = 0

input = [[i[0], int(i[1:])] for i in input]

for j in input:
    match j[0]:
        case 'R':
            direction += 90
        case 'L':
            direction -= 90
    match direction % 360:
        case 0 | 360:
            y += j[1]
        case 90 | -270:
            x += j[1]
        case 180 | -180:
            y -= j[1]
        case 270 | -90:
            x -= j[1]

print(abs(0 - x) + abs(0 - y))            
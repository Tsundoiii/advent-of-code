from math import dist, sqrt

input = [[x.split()[0], int(x.split()[1])] for x in open("input.txt").readlines()]

visited = []
head = {
    "x": 0,
    "y": 0
}
tail = {
    "x": 0,
    "y": 0
}

def move_tail():
    if dist(head.values(), tail.values()) > sqrt(2):
        if head["x"] == tail["x"]: #same columns
            if abs(tail["y"] + 1 - head["y"]) <= 1:
                tail["y"] += 1
            else:
                tail["y"] -= 1
        elif head["y"] == tail["y"]: #same row
            if abs(tail["x"] + 1 - head["x"]) <= 1:
                tail["x"] += 1
            else:
                tail["x"] -= 1
        else: #diagonal
            if head["x"] > tail["x"] and head["y"] > tail["y"]:
                tail["x"] += 1
                tail["y"] += 1
            elif head["x"] < tail["x"] and head["y"] > tail["y"]:
                tail["x"] -= 1
                tail["y"] += 1
            elif head["x"] < tail["x"] and head["y"] < tail["y"]:
                tail["x"] -= 1
                tail["y"] -= 1
            elif head["x"] > tail["x"] and head["y"] < tail["y"]:
                tail["x"] += 1
                tail["y"] -= 1

    if list(tail.values()) not in visited:
        visited.append(list(tail.values()))

for instruction in input:
    match instruction[0]:
        case 'R':
            for i in range(instruction[1]):
                head["x"] += 1
                move_tail()
        case 'L':
            for i in range(instruction[1]):
                head["x"] -= 1
                move_tail()
        case 'U':
            for i in range(instruction[1]):
                head["y"] += 1
                move_tail()
        case 'D':
            for i in range(instruction[1]):
                head["y"] -= 1
                move_tail()

print(len(visited))
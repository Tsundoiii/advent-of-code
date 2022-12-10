from math import dist, sqrt

input = [[x.split()[0], int(x.split()[1])] for x in open("input.txt").readlines()]

visited = []
knots = []
for i in range(10):
    knots.append({
        "x": 0,
        "y": 0
    })
head = knots[0]
tail = knots[9]

def move_tail(head, tail):
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

    return tail

for instruction in input:
    match instruction[0]:
        case 'R':
            for i in range(instruction[1]):
                head["x"] += 1
                current_head = head
                current_tail = knots[1]
                for j in range(1, len(knots)):
                    try:
                        knots[j] = move_tail(current_head, current_tail)
                        current_head = knots[j]
                        current_tail = knots[j + 1]
                    except IndexError:
                        pass
                if list(tail.values()) not in visited:
                    visited.append(list(tail.values()))
        case 'L':
            for i in range(instruction[1]):
                head["x"] -= 1
                current_head = head
                current_tail = knots[1]
                for j in range(1, len(knots)):
                    try:
                        knots[j] = move_tail(current_head, current_tail)
                        current_head = knots[j]
                        current_tail = knots[j + 1]
                    except IndexError:
                        pass
                if list(tail.values()) not in visited:
                    visited.append(list(tail.values()))
        case 'U':
            for i in range(instruction[1]):
                head["y"] += 1
                current_head = head
                current_tail = knots[1]
                for j in range(1, len(knots)):
                    try:
                        knots[j] = move_tail(current_head, current_tail)
                        current_head = knots[j]
                        current_tail = knots[j + 1]
                    except IndexError:
                        pass
                if list(tail.values()) not in visited:
                    visited.append(list(tail.values()))
        case 'D':
            for i in range(instruction[1]):
                head["y"] -= 1
                current_head = head
                current_tail = knots[1]
                for j in range(1, len(knots)):
                    try:
                        knots[j] = move_tail(current_head, current_tail)
                        current_head = knots[j]
                        current_tail = knots[j + 1]
                    except IndexError:
                        pass
                if list(tail.values()) not in visited:
                    visited.append(list(tail.values()))
print(len(visited))
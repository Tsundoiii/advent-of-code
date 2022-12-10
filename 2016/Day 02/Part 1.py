keys = {
    "U": -3,
    "D": 3,
    "L": -1,
    "R": 1
}

limits = {
    1: "UL",
    3: "UR",
    7: "DL",
    9: "DR"
}

input = open("input.txt").readlines()
previous_number = 5
code = []

for instruction in input:
    for movement in instruction:
        try:
            if not (previous_number in limits and movement in limits[previous_number]):
                previous_number += keys[movement]
        except KeyError:
            pass
    
    code.append(previous_number)

print(str(code))
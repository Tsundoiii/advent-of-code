plays = [play.split() for play in open("input.txt").readlines()]

score = 0

pairs = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

wins = {
    "X": "C",
    "Y": "A",
    "Z": "B"
}

points = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

for play in plays:
    if play[0] == wins[play[1]]:
        score += 6
    elif play[1] == pairs[play[0]]:
        score += 3

    score += points[play[1]]
        

print(score)

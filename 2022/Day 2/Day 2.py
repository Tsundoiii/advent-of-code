plays = [play.split() for play in open("input.txt").readlines()]

score = 0

pairs = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors"
}

xplay = {
    "A": "C",
    "B": "A",
    "C": "B"
}

zplay = {b: a for a, b in xplay.items()}

points = {
    "A": 1,
    "B": 2,
    "C": 3
}


for play in plays:
    match play[1]:
        case "X":
            p = xplay[play[0]]
        case "Y":
            p = play[0]
            score += 3
        case "Z":
            p = zplay[play[0]]
            score += 6

    score += points[p]

print(score)

from string import ascii_letters

input = [[ascii_letters.index(letter) for letter in line.rstrip()] for line in open("input.txt").readlines()]
START = []
END = []

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == 44:
            START.append(i)
            START.append(j)
        elif input[i][j] == 30:
            END.append(i)
            END.append(j)

print(START)
print(END)
from string import ascii_letters

input = open("input.txt").readlines()

groups = []

for i in range(0, len(input), 3):
    groups.append([input[i].rstrip(), input[i + 1].rstrip(), input[i + 2].rstrip()])

common = []

for group in groups:
    for letter in group[0]:
        if letter in group[1] and letter in group[2]:
            common.append(letter)
            break

priorities = {}

for i, letter in enumerate(ascii_letters):
    priorities.update({letter: i + 1})

print(sum([priorities[letter] for letter in common]))
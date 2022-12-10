from string import ascii_letters

input = [[x[:len(x) // 2], x[len(x) // 2:].rstrip()] for x in open("input.txt").readlines()]

common = []

for sack in input:
    for letter in sack[0]:
        if letter in sack[1]:
            common.append(letter)
            break

priorities = {}

for i, letter in enumerate(ascii_letters):
    priorities.update({letter: i + 1})

print(sum([priorities[letter] for letter in common]))
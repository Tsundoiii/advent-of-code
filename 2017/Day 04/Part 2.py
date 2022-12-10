from itertools import permutations

input = [line.split() for line in open("input.txt").readlines()]

valid = 0

def has_anagram(line):
    for word in line:
        perms = ["".join(anagram) for anagram in list(permutations(word))]
        perms.remove(word)
        for perm in perms:
            if perm in line:
                return True
        else:
            print(line)
            return False

for line in input:
    if not has_anagram(line):
        valid += 1

print(f"{valid = }")
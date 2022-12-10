input = open("input.txt").readlines()

checkVowels = lambda s : s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u") >= 3
def containsDuplicate(s):
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if s.count(letter + letter) > 0:
            return True
    return False
noBadString = lambda s : s.count("ab") + s.count("cd") + s.count("pq") + s.count("xy") == 0

count = 0

for s in input:
    if checkVowels(s) and containsDuplicate(s) and noBadString(s): count += 1

print(f"Count: {count}")
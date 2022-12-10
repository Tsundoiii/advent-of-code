ids = open("input.txt").readlines()

alphabet = "abcdefghijklmnopqrstuvwxyz"

twice = []
thrice = []

for id in ids:
    for letter in alphabet:
        if id.count(letter) == 2:
            twice.append(id)
            break
        if id.count(letter) == 3:
            thrice.append(id)
            break

print(f"Checksum is: {len(twice) * len(thrice)}")
print(len(twice))
print(len(thrice))
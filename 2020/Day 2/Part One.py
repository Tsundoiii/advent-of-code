lines = [x.split() for x in open('input.txt').readlines()]

for x in lines:
    x[0] = [int(y) for y in x[0].split('-')]
    x[1] = x[1].rstrip(':')

valid_count = 0

for z in lines:
    if z[0][0] <= z[2].count(z[1]) <= z[0][1]:
        valid_count += 1

print(f"The number of valid passwords is {valid_count}")
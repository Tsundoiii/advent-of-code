calories = [int(calorie) if calorie != "\n" else None for calorie in open("input.txt").readlines()]
amounts = []

cur = 0
for cal in calories:
    if cal != None:
        cur += cal
    else:
        amounts.append(cur)
        cur = 0

print(max(amounts))

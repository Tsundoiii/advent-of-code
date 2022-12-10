f = open('input.txt')
modulesFile = f.readlines()
modules = [int(x) for x in modulesFile]

fuelList = []

for x in modules:
    fuel = x // 3 - 2
    fuelList.append(fuel)

totalFuel = sum(fuelList)

print(f"The total fuel required is {totalFuel}")
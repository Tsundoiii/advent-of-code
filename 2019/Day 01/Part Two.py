modulesFile = open('input.txt').readlines()
modules = [int(x) for x in modulesFile]

def totalFuel(mass):
    calculateFuel = lambda mass : mass // 3 - 2
    if mass < 0:
        return 
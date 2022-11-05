diagnosticsFile = open('input.txt')
f = diagnosticsFile.readlines()

gamma = ""
epsilon = ""

zeroCount1 = 0
oneCount1 = 0

zeroCount2 = 0
oneCount2 = 0

zeroCount3 = 0
oneCount3 = 0

zeroCount4 = 0
oneCount4 = 0

zeroCount5 = 0
oneCount5 = 0

zeroCount6 = 0
oneCount6 = 0

zeroCount7 = 0
oneCount7 = 0

zeroCount8 = 0
oneCount8 = 0

zeroCount9 =0
oneCount9 = 0

zeroCount10 = 0
oneCount10 = 0

zeroCount11 = 0
oneCount11 = 0

zeroCount12 = 0
oneCount12 = 0

for x in f:
    if x[0] == "0":
        zeroCount1 += 1
    elif x[0] == "1":
        oneCount1 += 1

    if x[1] == "0":
        zeroCount2 += 1
    elif x[1] == "1":
        oneCount2 += 1

    if x[2] == "0":
        zeroCount3 += 1
    elif x[2] == "1":
        oneCount3 += 1

    if x[3] == "0":
        zeroCount4 += 1
    elif x[3] == "1":
        oneCount4 += 1

    if x[4] == "0":
        zeroCount5 += 1
    elif x[4] == "1":
        oneCount5 += 1

    if x[5] == "0":
        zeroCount6 += 1
    elif x[5] == "1":
        oneCount6 += 1

    if x[6] == "0":
        zeroCount7 += 1
    elif x[6] == "1":
        oneCount7 += 1

    if x[7] == "0":
        zeroCount8 += 1
    elif x[7] == "1":
        oneCount8 += 1

    if x[8] == "0":
        zeroCount9 += 1
    elif x[8] == "1":
        oneCount9 += 1

    if x[9] == "0":
        zeroCount10 += 1
    elif x[9] == "1":
        oneCount10 += 1

    if x[10] == "0":
        zeroCount11 += 1
    elif x[10] == "1":
        oneCount11 += 1

    if x[11] == "0":
        zeroCount12 += 1
    elif x[11] == "1":
        oneCount12 += 1

if zeroCount1 > oneCount1:
    gamma += "0"
elif oneCount1 > zeroCount1:
    gamma += "1"

if zeroCount2 > oneCount2:
    gamma += "0"
elif oneCount2 > zeroCount2:
    gamma += "1"

if zeroCount3 > oneCount3:
    gamma += "0"
elif oneCount3 > zeroCount3:
    gamma += "1"

if zeroCount4 > oneCount4:
    gamma += "0"
elif oneCount4 > zeroCount4:
    gamma += "1"

if zeroCount5 > oneCount5:
    gamma += "0"
elif oneCount5 > zeroCount5:
    gamma += "1"

if zeroCount6 > oneCount6:
    gamma += "0"
elif oneCount6 > zeroCount6:
    gamma += "1"

if zeroCount7 > oneCount7:
    gamma += "0"
elif oneCount7 > zeroCount7:
    gamma += "1"

if zeroCount8 > oneCount8:
    gamma += "0"
elif oneCount8 > zeroCount8:
    gamma += "1"

if zeroCount9 > oneCount9:
    gamma += "0"
elif oneCount9 > zeroCount9:
    gamma += "1"

if zeroCount10 > oneCount10:
    gamma += "0"
elif oneCount10 > zeroCount10:
    gamma += "1"

if zeroCount11 > oneCount11:
    gamma += "0"
elif oneCount11 > zeroCount11:
    gamma += "1"

if zeroCount12 > oneCount12:
    gamma += "0"
elif oneCount12 > zeroCount12:
    gamma += "1"

invertedBinary = {
    "0": "1",
    "1": "0"
}

intGamma = int(gamma, 2)

for x in gamma:
    epsilon = epsilon + invertedBinary[x]

intEpsilon = int(epsilon, 2)

print(f"Gamma is {gamma}")
print(f"The gamma rate is {intGamma}")

print(f"Epsilon is {epsilon}")
print(f"The epsilon rate is {intEpsilon}")

print(f"The power consumption is {intGamma * intEpsilon}")
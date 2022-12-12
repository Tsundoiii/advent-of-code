from math import floor

input = [x.splitlines() for x in open("test.txt").read().split("\n\n")]
operations = {
    "+": lambda x, y : x + y,
    "*": lambda x, y : x * y
}
monkeys = []
def operation(i):
    if i[2].split()[-1] != "old":
        return lambda old : operations[i[2].split()[-2]](old, int(i[2].split()[-1]))
    else:
        return lambda old : operations[i[2].split()[-2]](old, old)
def test(i):
    return lambda n : n % int(i[3].split()[-1]) == 0

for i in input:
    monkeys.append({
        "number": int(i[0].split()[-1].rstrip(":")),
        "items": [int(x) for x in i[1].lstrip("  Starting items: ").split(", ")],
        "operation": operation(i),
        "test": test(i),
        "true": int(i[4].split()[-1]),
        "false": int(i[5].split()[-1]),
        "inspected": 0
    })

for round in range(10000):
    for monkey in monkeys:
        for item in monkey["items"]:
            worry = monkey["operation"](item)
            if monkey["test"](worry):
                monkeys[monkey["true"]]["items"].append(worry)
            else:
                monkeys[monkey["false"]]["items"].append(worry)

            monkey["inspected"] += 1
        else:
            monkey["items"].clear()


inspections = []
for m in monkeys:
    inspections.append(m["inspected"])

print(sorted(inspections)[-1] * sorted(inspections)[-2])
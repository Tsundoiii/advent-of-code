frequencies = [int(x) for x in open('input.txt').readlines()]

frequency = 0

for freq in frequencies:
    frequency += freq

print(f"The resulting frequency is {frequency}")
f = open('input.txt')
directions = f.read()

floor = 0

for x in directions:
  if x == '(':
    floor += 1
  elif x == ')':
    floor -= 1

print(f"Santa is on floor {floor}")
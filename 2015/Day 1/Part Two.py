f = open('input.txt')
directions = f.read()

floor = 0
index = 0

for x in directions:
  if floor == -1:
    break
  if x == '(':
    floor += 1
    index += 1
  elif x == ')':
    floor -= 1
    index += 1

print(f"Santa enters the basement at {index}")
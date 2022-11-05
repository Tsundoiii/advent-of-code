passwords = []
valid = []

for i in range(248345, 746316):
    s = str(i)
    last = s[0]
    validNum = True
    for digit in s:
        if int(digit) < int(last):
            validNum = False
            break
        last = digit
    if validNum:
        passwords.append(i)

for password in passwords:
    s = str(password)
    last = s[0]
    for digit in s:
        if int(digit) == int(last):
            valid.append(password)
            break
        last = digit

print(f"Valid passwords: {len(passwords)}")
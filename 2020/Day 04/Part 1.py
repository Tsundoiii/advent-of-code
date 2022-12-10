passports = open("input.txt").read().split("\n\n")

requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def splitPassport(passport):
    passport = passport.replace(" ", "\n")
    passport = passport.split("\n")
    return passport

def genDict(passport):
    newPassport = {}
    for field in passport:
        newPassport.update({field.split(":")[0]: field.split(":")[1]})
    return newPassport

def isValid(passport):
    global requiredFields
    for field in requiredFields:
        for pField in passport:
            if field not in passport:
                return False
    return True

passports = [genDict(splitPassport(passport)) for passport in passports]
valid = []

for passport in passports:
    if isValid(passport):
        valid.append(passport)

print(f"Valid passports: {len(valid)}")
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
valids = []

for passport in passports:
    if isValid(passport):
        valids.append(passport)

def validData(passport):
    byr = lambda year : 1920 <= int(year) <= 2002
    iyr = lambda year : 2010 <= int(year) <= 2020
    eyr = lambda year : 2020 <= int(year) <= 2030
    def hgt(height):
        if height.endswith("cm"): return 150 <= int(height.rstrip("cm")) <= 193
        if height.endswith("in"): return 59 <= int(height.rstrip("in")) <= 76
    def hcl(color):
        if len(color) != 7: return False
        if not color.startswith("#"): return False
        for char in color.lstrip("#"):
            if not ((char in "0123456789") or (char in "abcdef")): return False
        return True
    ecl = lambda color : color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pid = lambda id : len(id) == 9
    return byr(passport["byr"]) and iyr(passport["iyr"]) and eyr(passport["eyr"]) and hgt(passport["hgt"]) and hcl(passport["hcl"]) and ecl(passport["ecl"]) and pid(passport["pid"])

for passport in valids:
    if not validData(passport): valids.remove(passport)

print(f"Valid passports: {len(valids)}")
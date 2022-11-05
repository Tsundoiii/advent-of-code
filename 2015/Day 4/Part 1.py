from hashlib import md5

for i in range (1000000):
    if md5(f"ckczppom{i}".encode('utf-8')).hexdigest().startswith("00000"):
        print(f"{i = }")
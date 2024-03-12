def getXOR(name):
    result = 0
    for i in name:
        result ^= ord(i)
    return result

def

print(getXOR("abd"))
print(getXOR("bda"))

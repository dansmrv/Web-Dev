def xor(a,b):
    if (a or b) and a is not b:
        return 1
    else: return 0

a = int(input())
b = int(input())

print(xor(a,b))
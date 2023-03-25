def minimun(a,b,c,d):
    minn = a
    if b < a:
        minn = b
    if c < b:
        minn = c
    if d < c:
        minn = d
    return minn

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(minimun(a,b,c,d))
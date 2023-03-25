def is_power(a):
    poww=0
    x = 1
    while x<=a:
        if x == a:
            return True
        x=pow(2,poww)
        poww+=1
    return False
num=int(input())

if is_power(num):
    print("YES")
else: print("NO")
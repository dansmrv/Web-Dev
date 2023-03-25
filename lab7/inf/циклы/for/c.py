a = int(input())
b = int(input())

for x in range(a,b+1):
    sqrt=pow(x,1/2)
    if sqrt==round(sqrt):
        print(x)
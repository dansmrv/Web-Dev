num=input()
power = 0
a = 0

for x in range(len(num)-1,-1,-1):
    if num[x] == '1':
        a += pow(2,power)
    power += 1
print(a)

a = int(input())
b = int(input())

for num in range(a, b + 1):
    if (num % 2 == 0) and (a<b):
        print(num, end = " ")
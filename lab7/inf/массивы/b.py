size = int(input())
arr = []

for x in range(size):
    num = int(input())
    arr.append(num)

for el in arr: 
    if el%2==0:
        print(el)
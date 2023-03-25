size = int(input())
arr = []
cnt = 0

for x in range(size):
    num = int(input())
    arr.append(num)

for el in arr:
    if el>0:
        cnt+=1
    
print(cnt)
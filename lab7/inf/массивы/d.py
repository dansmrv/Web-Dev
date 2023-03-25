size = int(input())
arr = []
cnt = 0

for x in range(size):
    num = int(input())
    arr.append(num)

for x in range(1,size):
    if arr[x]>arr[x-1]:
        cnt+=1
    
print(cnt)
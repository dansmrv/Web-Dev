num = int(input())
cnt=0

for x in range(1,num+1):
    if num%x==0:
        cnt+=1
print(cnt)
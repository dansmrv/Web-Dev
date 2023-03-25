size = int(input())
arr = []
ans = "NO"

def check(a,b,c):
    if a>0 and b>0 and c>0 or a<0 and b<0 and c<0:
        return True
    else:
        return False

for x in range(size):
    num = int(input())
    arr.append(num)

for x in range(1,size-1):
    if check(arr[x-1],arr[x],arr[x+1]):
        ans="YES"
    
print(ans)
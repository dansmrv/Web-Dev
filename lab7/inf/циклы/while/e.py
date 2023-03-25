def is_it_power(a):
    poww=0
    p2 = 1
    while p2<a:
        poww+=1
        p2=pow(2,poww)
    return poww


num = int(input())
print(is_it_power(num))
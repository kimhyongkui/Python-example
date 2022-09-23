N = int(input())
m = 2
while N!=1:
    if N%m == 0:
        N = N/m
        print(m)
    else:
        m += 1

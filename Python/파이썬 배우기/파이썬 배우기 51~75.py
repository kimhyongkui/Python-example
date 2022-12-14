# 51 1977
M = int(input())
N = int(input())
sum = 0
min = 0

for i in range(1, 101):
    if M <= i*i and N >= i*i:
        if sum == 0:
            min = i*i
        sum += i*i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)

# 52 11098
n = int(input())
for _ in range(n):
    player = []
    maxPr = 0
    for _ in range(int(input())):
        player.append(list(input().split()))
    for pr in player:
        price = int(pr[0])
        if maxPr < price:
            maxPr = price
    for n in player:
        if n[0] == str(maxPr):
            print(n[1])

# 53 5635
import sys
input = sys.stdin.readline

n = int(input())
st = []
for _ in range(n):
    n, d, m, y = input().split()
    st.append([n, int(d), int(m), int(y)])
st.sort(key=lambda x: (x[3], x[2], x[1]))
print(st[-1][0])    # 가장 나이 적은 사람
print(st[0][0])     # 가장 나이 많은 사람

# 54 1408
a1,b1,c1=input().split(':')
a1=int(a1)
b1=int(b1)
c1=int(c1)
a2,b2,c2=input().split(':')
a2=int(a2)
b2=int(b2)
c2=int(c2)

hour=a2-a1+23
min=b2-b1+59
sec=c2-c1+60

if sec>=60:
    sec-=60
    min+=1
if min>=60:
    min-=60
    hour+=1
if hour>=24:
    hour-=24
print('%02d:%02d:%02d' % (hour,min,sec))

# 55 2741
n = int(input())

for i in range(1,n+1): #1~n까지 범위 -> 1,n+1 지정
    print(i)

# 56 2742
a = int(input())
for i in range(a, 0, -1):
    print(i)

# 57 2739
n = int(input())

for i in range(1, 10):
    print(n, "*", i, "=", n*i)

# 58 2438
N=int(input())
for i in range(1, N+1):
    print("*"*i)

# 59 2439
x = int(input())
for i in range(1, x+1):
    print(' '*(x-i)+"*"*i)

# 60 2440
x = int(input())
for i in range(x, 0, -1):
    print("*"*i)

# 61 2441
n = int(input())

for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)

# 62 8393
n = int(input())
sum = 0

for i in range(1, n + 1):
    sum += i

print(sum)

# 63 2609
a, b = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(a, b), a * b // gcd(a, b))

# 64 2748
N = int(input())
A = [i for i in range(N + 1)]
A[1] = 1

for i in range(2, N + 1):
    A[i] = A[i - 1] + A[i - 2]

print(A[-1])

# 65 5565
N = int(input())
A = [i for i in range(N + 1)]
A[1] = 1

for i in range(2, N + 1):
    A[i] = A[i - 1] + A[i - 2]

print(A[-1])

# 66 5565
num=int(input(''))

sum=0

for i in range(9):
    n=int(input(''))
    sum=sum+n

print(num-sum)

# 67 10950
T = int(input())

for i in range(T):
    A,B = map(int,input().split())
    print(A+B)

# 68 10952
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print(a + b)

# 69 10984
for _ in range(int(input())):
    C = G = 0
    for i in range(int(input())):
        c, g = map(float, input().split())
        C += c
        G += c*g
    print("%d %.1f" %(C, G/C))

# 70 10833
import sys
input = sys.stdin.readline

ans = 0
for _ in range(int(input())):
    a,b = map(int,input().split())
    ans += b%a
print(ans)

# 71 2442
n = int(input())

count = n - 1
for i in range(1, 2*n, 2) :
  print(' ' * count, end='')
  print('*' * i)
  count -= 1

# 72 2443
n = int(input())

for i in range(n, 0, -1) :
  print(' '*(n-i) + '*'*(2*i-1))

# 73 2444
n = int(input())

for i in range(1, n) :
  print(' '*(n-i) + '*'*(2*i-1))

for i in range(n, 0, -1) :
  print(' '*(n-i) + '*'*(2*i-1))

# 74 2522
N = int(input())
for i in range(1, N+1):
    print(' '*(N-i) + '*'*i)
for i in range(1, N):
    print(' '*(i) + '*'*(N-i))

# 75 2523
n = int(input())
for i in range(1, n + 1):
    print("*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i)
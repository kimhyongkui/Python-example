# 76 9325
t = int(input())
for i in range(t):
    op_price = 0
    price = int(input())
    option = int(input())
    for j in range(option):
        a, b = map(int, input().split())
        op_price += a * b
    print(price + op_price)

# 77 2445
n = int(input())
for i in range(1,n+1):
    print("*" * i + " " * 2*(n-i) + "*" * i)
for j in range(1,n):
    print("*"* (n-j) + " " * 2*j + "*" * (n-j))

# 78 2446
inputNum = int(input())

for i in range(inputNum):
    print(' '*i, '*'*((inputNum-i)*2-1))

for i in range(inputNum-2, -1, -1):
    print(' '*i, '*'*((inputNum-i)*2-1))

# 79 2010
import sys
n = int(sys.stdin.readline())
sum = 0
for i in range(n):
    sum += int(sys.stdin.readline())
print(sum - (n - 1))

# 80 5522
n=0
for i in range(5):
    n+=int(input())
print(n)

# 81 10178
t = int(input())

for i in range(t):
    c, f = map(int, input().split())
    print("You get {0} piece(s) and your dad gets {1} piece(s).".format(c // f, c % f))

# 82 9295
t = int(input())

for i in range(1, t + 1) :
  a, b = map(int, input().split())
  print("Case ", i, ": ", a + b, sep='')

# 83 10569
x = int(input())
for i in range(x):
    a, b = map(int, input().split())
    c = 2 - a + b
    print(c)

# 84 2921
n = int(input())
sum = 0
for i in range(0, n + 1):
    for j in range(i, n + 1):
        sum += i + j
print(sum)

# 85 10995
N = int(input())
for i in range(N):
    print("* "*N if i%2 == 0 else " *"*N)
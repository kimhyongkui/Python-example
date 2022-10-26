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
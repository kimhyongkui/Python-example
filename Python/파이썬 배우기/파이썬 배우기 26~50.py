# 26 2753
a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print(1)
else:
    print(0)

# 27 10039
sum = 0
for i in range(5):
    x = int(input())
    if x < 40:
        sum += 40
    else:
        sum += x
print(int(sum / 5))

# 28 1934
num = int(input())
for i in range(num):
    a, b = map(int, input().split())
    A, B = a, b
    while a != 0:
        b = b % a
        a, b = b, a
        # print(a,b)
    gcd = b
    lcm = A * B // b
    print(lcm)

# 29 2480
a, b, c = map(int, input().split())

if a == b == c :
  print(10000 + a * 1000)
elif a == b :
  print(1000 + a * 100)
elif a == c :
  print(1000 + a * 100)
elif b == c :
  print(1000 + b * 100)
else :
  print(max(a, b, c) * 100)

# 30 4101
numbers = []
while True:
    a = list(map(int, input().split()))
    if a == [0, 0]:
        break
    numbers.append(a)
for number in numbers:
    if number[0] > number[1]:
        print("Yes")
        continue
    print("No")

# 31 10156
k, n, m = list(map(int, input().split()))

print(((k*n)-m) if ((k*n)-m) >= 0 else 0)

# 32 3009
x_ = []
y_ = []
for i in range(3):
        x, y = map(int, input().split())
        x_.append(x)
        y_.append(y)
for i in range(3):
        if x_.count(x_[i]) == 1:
                x = x_[i]
        if y_.count(y_[i]) == 1:
                y = y_[i]
print(x, y)

# 33 2476
n = int(input())
maxMoney = 0
for i in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        maxMoney = max(maxMoney, 10000 + a * 1000)
    elif a == b:
        maxMoney = max(maxMoney, 1000 + a * 100)
    elif a == c:
        maxMoney = max(maxMoney, 1000 + a * 100)
    elif b == c:
        maxMoney = max(maxMoney, 1000 + b * 100)
    else:
        maxMoney = max(maxMoney, max(a, b, c) * 100)

print(maxMoney)

# 34 2754
score = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
       'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
       'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
       'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
       'F': 0.0}

print(score[str(input())])

# 35 2884
H, M = map(int,input().split())
if M > 44:
    print(H, M-45)
elif M<45 and H>0:
    print(H-1,M+15)
else:
    print(23,M+15)

36
37
38
39
40
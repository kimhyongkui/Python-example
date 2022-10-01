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

# 36 7567
plates = input()
ans = 10 # 처음 그릇을 바닥에 놓았을 때 높이 10cm

for i in range(1, len(plates)):
    # 두 번째 그릇부터 이전 그릇과 비교 시작
    if plates[i] == plates[i - 1]:
        ans += 5 # 같은 방향이면 5cm 추가
    else:
        ans += 10 # 다른 방향이면 10cm 추가

print(ans)

# 37 5063
tc = int(input())

for _ in range(tc) :
  r, e, c = map(int, input().split())

  if e - c > r :
    print("advertise")
  elif e - c == r :
    print("does not matter")
  else :
    print("do not advertise")

# 38 10102
num = int(input())
result = input()
a = b = 0
for i in range(0, num):
    if (result[i] == 'A'):
        a = a + 1
    elif (result[i] == 'B'):
        b = b + 1

if (a > b):
    print('A')
elif (a < b):
    print('B')
else:
    print('Tie')

# 39 10886
import sys
input = sys.stdin.readline

a,b = 0,0
for _ in range(int(input())):
    if int(input()) == 0:
        a+=1
    else:
        b+=1
if a > b:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")

# 40 10988
w = input()
x = 1
for i in range(len(w)//2):
    if w[i] != w[-i-1]:
        print(0)
        x = 0
        break
if x == 1: print(x)

# 41 5086
while (1):
    x, y = map(int, input().split())

    if x == 0 and y == 0:
        break

    if x < y and y % x == 0:
        print("factor")
    elif x > y and x % y == 0:
        print("multiple")
    else:
        print("neither")

# 42 5717
while True:
    a,b = map(int,input().split(" "))
    if a==0 and b==0:
        break
    print(a+b)

# 43 9610
li = [0]*5
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        li[4] += 1
    elif x > 0 and y > 0:
        li[0] += 1
    elif x < 0 and y > 0:
        li[1] += 1
    elif x < 0 and y < 0:
        li[2] += 1
    else:
        li[3] += 1
for i in range(4):
    print(f"Q{i+1}: {li[i]}")
print(f"AXIS: {li[4]}")

# 44 8958
n=int(input())
for i in range(0,n):
    count,c=0,1
    s=list(input())
    for j in s:
        if j=='O':
            count+=c
            c+=1
        else:
            c=1
    print(count)

# 45 9506
while True:
    n = int(input())
    if n == -1: # 입력 값이 -1이면 반복문 종료
        break;
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    if sum(arr) == n:
        print(n, " = ", " + ".join(str(i) for i in arr), sep="")
    else:
        print(n, "is NOT perfect.")
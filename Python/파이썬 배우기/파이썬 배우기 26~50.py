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
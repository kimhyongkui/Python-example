# # 1 Hello world! 출력
# print("Hello World!")
#
# # 2
# a, b = map(int, input().split())
# print(a+b)
#
# # 3 AxB
# a, b = map(int, input().split())
# print(a*b)
#
# # 4 A-B
# a, b = map(int, input().split())
# print(a-b)
#
# # 5 A/B
# a, b = map(int, input().split())
# print(a/b)
#
# # 6 A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램
# a, b = map(int, input().split())
# print(a+b) #덧셈
# print(a-b) #뺄셈
# print(a*b) #곱셉
# print(a//b) #몫
# print(a%b) #나머지
#
# # 7
# a,b,c = map(int, input().split())
# print((a+b)%c, ((a%c)+(b%c))%c, (a*b)%c, ((a%c)*(b%c))%c, sep='\n')
#
# # 8 2558
# a = int(input())
# b = int(input())
# print(a+b)
#
# # 9 2588
# A = int(input())
# B = int(input())
#
# print(A * (B % 10))
# print(A * (B % 100 // 10))
# print(A * (B // 100))
# print(A * B)
#
# # 10 3046
# r1, s=input().split()
# print(int(s)*2-int(r1))
#
# # 11 2163
# N, M = map(int, input().split())
# print(N-1 + (M-1)*N)
#
# # 12 11021
# t = int(input())
#
# for i in range(1, t+1): # 1부터 t까지
#     a, b = map(int, input().split())
#     print(f"Case #{i}: {a+b}")
#
# # 13 11022
# T = int(input())
#
# for i in range(1, T+1):
#     A, B = map(int, input().split())
#     print(f"Case #{i}: {A} + {B} = {A+B}")
#
# # 14 10699
# import datetime
# print(str(datetime.datetime.now())[:10])
#
# # 15 7287
# print("자신이 맞춘 개수")
# print("자신의 아이디")

# 16 2525
h, m = map(int, input().split())
timer = int(input())

h += timer // 60
m += timer % 60

if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24

print(H,M)

# 17 2530
h,m,s = map(int,input().split())
t = int(input())

s += t
m += s//60
h += m//60
print(h%24,m%60,s%60)

# 18 2914
A, I = list(map(int, input().split()))
print((I - 1) * A + 1)
# 평균값에 1을 빼고 곡의 개수 (A)를 곱해준 뒤 1을 더해준다.

# 19 5355
t = int(input())

for _ in range(t):
    a = list(input().split())
    num = float(a.pop(0))
    for i in range(len(a)):
        if a[i] == '@':
            num *= 3
        elif a[i] == '%':
            num += 5
        elif a[i] == '#':
            num -= 7

    print("%0.2f" % num)

# 20 2675
t = int(input())
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)

# 21 2935
A = int(input())
B = str(input())
C = int(input())

if B == '*':
    print(A*C)
else:
    print(A+C)

# 22 9498
score = int(input())

if score >= 90 :
    print('A')
elif score >= 80 :
    print('B')
elif score >= 70 :
    print('C')
elif score >= 60 :
    print('D')
else:
    print('F')

# 23 10817
num_list = list(map(int, input().split()))
num_list.sort()
print(num_list[1])

# 24 11653
N = int(input())
m = 2
while N!=1:
    if N%m == 0:
        N = N/m
        print(m)
    else:
        m += 1

# 25 1789
s = int(input())
n = 1                          # 최대값을 구하는 문제이므로 1부터 차례대로 더해 s보다 커지면 그 개수에서 1을 뺀다.
while n * (n + 1) / 2 <= s:    # n*(n+1)/2 = 1부터 n까지의 합의 공식
    n += 1
print(n - 1)

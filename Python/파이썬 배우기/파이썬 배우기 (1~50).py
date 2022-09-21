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

# 12 11021
# t = int(input())
#
# for i in range(1, t+1): # 1부터 t까지
#     a, b = map(int, input().split())
#     print(f"Case #{i}: {a+b}")

# 13 11022
T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    print(f"Case #{i}: {A} + {B} = {A+B}")

# 14 10699
import datetime
print(str(datetime.datetime.now())[:10])

# 15 7287
print("자신이 맞춘 개수")
print("자신의 아이디")

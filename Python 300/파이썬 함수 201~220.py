# 201
def print_coin():
    print("비트코인")

# 202
print_coin()

# 203
# for i in range(100):
#     print_coin()

# 204
def print_coins():
    for i in range(100):
        print("비트코인")

# 205
# hello()
# def hello():
#     print("Hi")
# 에러가 발생하는 이유 : 함수가 정의되기전에 호출되었기 때문에

# 206
def message() :
    print("A")
    print("B")

message()
print("C")
message()

# 207
print("A")

def message() :
    print("B")

print("C")
message()

# 208
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()

# 209
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

# 210
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()

# 211
def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")

# 212
def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8)

# 213
# def 함수(문자열) :
#     print(문자열)
# 함수()
# 함수에 정의와 다르게 함수를 호출하고 있다. 함수를 호출할 때 하나의 파라미터를 입력해야한다.

# 214
# def 함수(a, b) :
#     print(a + b)
#
# 함수("안녕", 3)
# 정의된 함수는 같은 타입의 두 개의 값을 입력 받아 덧셈 연산을 적용하려는 의도로 설계됐습니다.
# 하지만 함수를 호출 할때 문자열과 숫자를 입력해서 문자열과 숫자는 더할 수 없다는 에러가 발생합니다

# 215
def print_with_smile (string):
    print(string + ":D")

# 216
print_with_smile("안녕하세요")

# 217
def print_upper_price(price) :
    print(price * 1.3)

# 218
def print_sum (a, b) :
    print (a + b)

# 219
def print_arithmetic_operation(a, b):
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)
print_arithmetic_operation(3, 4)

# 220
def print_max(a, b, c) :
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)

def print_max(a, b, c):
    if a>b and a>c:
        print(a)
    elif b>c and b>a:
        print(b)
    else:
        print(c)
print_max(10, 1, 2)
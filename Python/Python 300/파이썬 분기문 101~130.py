#101
#파이썬에서 True or False를 갖는 데이터 타입 = bool

#102
print(3 == 5)
False

#103
print(3 < 5)
True

#104
x = 4
print(1 < x < 5)
True

#105
print((3 == 3) and (4 != 3))

#106
# print(3 => 4) 지원하지 않는 연산자

#107
if 4 < 3:
    print("Hello World")
#조건 만족못해서 출력 안됨

#108
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")

#109
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")

#110
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")

#111
user = input("입력:")
print(user * 2)

#112
number = input("숫자를 입력하세요:")
print(int(number) + 10)

#113
user = input("")
if int(user) % 2 == 0:
    print("짝수")
else:
    print("홀수")

#114
user = input("입력값: ")
num = 20 + int(user)
if num > 255:
    print(255)
else:
    print(num)

#115
user = input("입력값: ")
num = int(user) - 20
if num > 255:
    print(255)
elif num < 0:
    print(0)
else:
    print(num)

#116
time = input("현재시간:")
if time[-2:] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다")

#117
fruit = ["사과", "포도", "홍시"]
user = input("좋아하는 과일은?")
if user in fruit:
    print("정답입니다")
else:
    print("오답입니다")

#118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
종목 = input("종목명: ")
if 종목 in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

#119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("제가좋아하는계절은: ")
if user in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

#120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은?")
if user in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")

#121
user = input("")
if user.islower():
    print(user.upper())
else:
    print(user.lower())

#122
score = input("score: ")
score = int(score)
if 81 <= score <= 100:
    print("grade is A")
elif 61 <= score <= 80:
    print("grade is B")
elif 41 <= score <= 60:
    print("grade is C")
elif 21 <= score <= 40:
    print("grade is D")
else:
    print("grade is E")

#123
환율 = {"달러": 1167,
        "엔": 1.096,
        "유로": 1268,
        "위안": 171}
user = input("입력: ")
num, currency = user.split()
print(float(num) * 환율[currency], "원")

#124
num1 = input("input number1: ")
num2 = input("input number2: ")
num3 = input("input number3: ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)

#125
number = input("휴대전화 번호 입력: ")
num = number.split("-")[0]
if num == "011":
    com = "SKT"
elif num == "016":
    com = "KT"
elif num == "019":
    com = "LGU"
else:
    com = "알수없음"
print(f"당신은 {com} 사용자입니다.")

#126
우편번호 = input("우편번호: ")
우편번호 = 우편번호[:3]
if 우편번호 in ["010", "011", "012"]:
    print("강북구")
elif 우편번호 in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")

#127
주민번호 = input("주민등록번호: ")
주민번호 = 주민번호.split("-")[1]
if 주민번호[0] == "1" or 주민번호[0] == "3":
    print("남자")
else:
    print("여자")

#128
주민번호 = input("주민등록번호: ")
뒷자리 = 주민번호.split("-")[1]
if 0 <= int(뒷자리[1:3]) <= 8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")

#129
num = input("주민등록번호: ")
계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
        int(num[11])* 4 + int(num[12]) * 5
계산2 = 11 - (계산1 % 11)
계산3 = str(계산2)

if num[-1] == 계산3[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

#130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")
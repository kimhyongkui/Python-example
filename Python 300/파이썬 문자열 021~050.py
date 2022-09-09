#21
letters = "python"
print(letters[0], letters[2])

#22
license_plate = "24가 2210"
print(license_plate[-4:])

#23
string = "홀짝홀짝홀짝"
print(string[::2])
#콜론 왼쪽 숫자 = 우리가 추출하기 원하는 시작 인덱스
#콜론 오른쪽에 써주는 숫자 = 우리가 추출하기 원하는 끝 인덱스 + 1

#24
string = "PYTHON"
print(string[::-1])

#25
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-"," ")
print(phone_number1)

#26
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-","")
print(phone_number1)

#27
url = "http://naver.com"
url_split = url.split('.')
print(url_split[-1])

#28
# lang = 'python'
# lang [0] = 'P'
# print(lang)
# 문자열은 수정할 수 없습니다. 실행 결과를 확인해보면 문자열이 할당(assignment) 메서드를 지원하지 않음을 알 수 있습니다.

#29
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)

#30
string = 'abcd'
string.replace('b', 'B')
print(string)
# abcd가 그대로 출력됨 왜냐하면 문자열은 변경할 수 없기 때문이다.

#31
a = "3"
b = "4"
print(a+b)

#32
print("Hi" * 3)

#33
print('-' * 80)

#34
t1 = 'python'
t2 = 'java'
t3 = t1 + " " + t2 + " "
print(t3 * 4)

#35
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

#36
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

#37
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

#38
상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",", "")
타입변환 = int(컴마제거)
print(타입변환, type(타입변환))

#39
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

#40
data = "   삼성전자   "
data1 = data.strip()
print(data1)

#41
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)

#42
ticker = "BTC_KRW"
ticker1 = ticker.lower()
print(ticker1)

#43
a = "hello"
a = a.capitalize()
print(a)

#44
file_name = "보고서.xlsx"
x = file_name.endswith("xlsx")
print(x)
# endsWith 메서드

#45
file_name = "보고서.xlsx"
x = file_name.endswith(("xlsx", "xls"))
print(x)

#46
file_name = "2020_보고서.xlsx"
x = file_name.startswith("2020")
print(x)

#47
a = "hello world"
a1 = a.split()
print(a1)

#48
ticker = "btc_krw"
ticker1 = ticker.split("_")
print(ticker1)

#49
date = "2022-08-18"
date1 = date.split("-")
print(date1)

#50
date = "039490    "
date1 = date.rstrip()
print(date1)
# rstrip()메소드
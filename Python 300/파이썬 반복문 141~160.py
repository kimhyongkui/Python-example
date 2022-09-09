# 141
판매가 = [100, 200, 300]
for 결제가격 in 판매가:
    print(결제가격 + 10)

# 142
리스트 = ["김밥", "라면", "튀김"]
for 메뉴 in 리스트:
    print("오늘의 메뉴: " + 메뉴)

# 143
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for 종목명 in 리스트:
    길이 = len(종목명)
    print(길이)

# 144
리스트 = ['dog', 'cat', 'parrot']
for 종류 in 리스트:
    print(종류, len(종류))

# 145
리스트 = ['dog', 'cat', 'parrot']
for 이름 in 리스트:
  print(이름[0])

# 146
리스트 = [1, 2, 3]
for 변수 in 리스트:
    print("3 x " + str(변수))

# 147
리스트 = [1, 2, 3]
for 변수 in 리스트:
    print("3 x ", 변수, "=", 3 * 변수)

# 148
리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[1:]:
    print(변수)

# 149
리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[: :2]:
  print(변수)

# 150
리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[: :-1]:
  print(변수)

# 151
리스트 = [3, -20, -3, 44]
for 변수 in 리스트:
    if 변수 < 0:
        print(변수)

# 152
리스트 = [3, 100, 23, 44]
for 변수 in 리스트:
  if 변수 % 3 == 0:
    print(변수)

# 153
리스트 = [13, 21, 12, 14, 30, 18]
for 변수 in 리스트:
  if (변수 < 20) and (변수 % 3 == 0):
    print(변수)

# 154
리스트 = ["I", "study", "python", "language", "!"]
for 변수 in 리스트:
  if len(변수) >= 3:
    print(변수)

# 155
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
  if 변수.isupper():
    print(변수)

# 156
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
  if 변수.isupper() == False:
    print(변수)

# 157
리스트 = ['dog', 'cat', 'parrot']
for 변수 in 리스트:
  첫글자 = 변수[0]              # 1)
  대문자 = 첫글자.upper()     # 2)
  print(대문자 + 변수[1:])      # 3)

# 158
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for 변수 in 리스트:
  split = 변수.split(".")
  print(split[0])

# 159
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
  split = 변수.split(".")
  if split[1] == "h":
    print(변수)

# 160
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
  split = 변수.split(".")
  if (split[1] == "h") or (split[1] == "c"):
    print(변수)

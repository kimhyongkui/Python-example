# 161
for i in range(100):
    print (i)

# 162
for x in range(2002, 2051, 4):
    print(x)

# 163
for num in range(3, 31, 3):
    print(num)

# 164
for i in range(100):
    print(99-i)

# 165
for num in range(10):
    print(num / 10)

# 166
for i in range(1, 10):
    print(3, "x", i, "=", 3 * i)

# 167
num = 3
for i in range(1, 10, 2):
    print(num, "x", i, "=", num * i)

# 168
plus = 0
for i in range(1, 11):
    plus += i
print("합 :", plus)

# 169
hab = 0
for i in range(1, 11, 2):
    hab += i
print("합 :", hab)

# 170
result = 1
for i in range(1, 11):
    result *= i
print(result)

# 171
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(price_list[i])

price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])
# len()함수를 이용하면 price_list가 변해도 코드의 수정이 필요없음. 더 좋은 코드

# 172
price_list = [32100, 32150, 32000, 32500]
for i, data in enumerate(price_list):
    print(i, data)

# 173
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print((len(price_list) - 1) - i, price_list[i])

# 174
for i in range(1, 4):
    print(90 + 10 * i, price_list[i])

# 175
my_list = ["가", "나", "다", "라"]
for i in range(len(my_list) - 1):
    print(my_list[i], my_list[i+1])

for i in range(1, len(my_list)):
    print(my_list[i-1], my_list[i])

# 176
my_list = ["가", "나", "다", "라", "마"]
for i in range(len(my_list) - 2):
    print(my_list[i], my_list[i+1], my_list[i+2])

for i in range(1, len(my_list) - 1):
    print(my_list[i-1], my_list[i], my_list[i+1])

for i in range(2, len(my_list)):
    print(my_list[i-2], my_list[i-1], my_list[i])

# 177
my_list = ["가", "나", "다", "라"]
for i in range(len(my_list) - 1, 0, -1):
    print(my_list[i], my_list[i-1])

for i in range(len(my_list) - 1):
    print(my_list[len(my_list) - 1 - i], my_list[len(my_list) - 2 - i])

# 178
my_list = [100, 200, 400, 800]
for i in range(len(my_list) - 1):
    print(abs(my_list[i+1] - my_list[i]))

# 179
my_list = [100, 200, 400, 800, 1000, 1300]

for i in range(0, len(my_list) - 2):
    print(abs(my_list[i] + my_list[i+1] + my_list[i+2]) / 3)

# 180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []
for i in range(len(low_prices)) :
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)
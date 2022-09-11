# # 221
# def print_reverse(string):
#     print(string[::-1])
# print_reverse("python")
#
# # 222
# def print_score(score_list):
#     print(sum(score_list)/len(score_list))
# print_score ([1, 2, 3])
#
# # 223
# def print_even(my_list):
#     for v in my_list:
#         if v % 2 == 0:
#             print(v)
# print_even([1,3,2,10,12,11,15])
#
# # 224
# def print_keys(dic):
#     for keys in dic.keys():
#         print(keys)
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})
#
# # 225
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# def print_value_by_key(my_dict, key):
#     print(my_dict[key])
# print_value_by_key(my_dict, "10/26")
#
# # 226
# def print_5xn(line):
#     count_num = int(len(line) / 5)
#     for x in range(count_num + 1) :
#         print(line[x * 5: x * 5 + 5])
# print_5xn("아이엠어보이유알어걸")
#
# # 227
# def print_mxn(line, num):
#     chunk_num = int(len(line) / num)
#     for x in range(chunk_num + 1) :
#         print(line[x * num: x * num + num])
# print_mxn("아이엠어보이유알어걸", 3)
#
# # 228
# def calc_monthly_salary(annual_pay) :
#     monthly_pay = int(annual_pay / 12)
#     return monthly_pay
# calc_monthly_salary(12000000)
#
# # 229
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
#
# my_print(a=100, b=200)
#
# # 230
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
#
# my_print(b=100, a=200)
#
# # 231
# def n_plus_1 (n) :
#     result = n + 1
#
# n_plus_1(3)

# 232
# def make_url(string) :
#     url = "www." + string + ".com"
#     return url
# a = make_url("naver")
# print(a)

# 233
def make_list (string) :
    my_list = []
    for 변수 in string :
        my_list.append(변수)
    return my_list
print(make_list("abcd"))

# 234
def pickup_even(items):
    result = []
    for item in items:
        if item % 2 == 0:
            result.append(item)
    return result

# 235
def convert_int (string) :
    return int(string.replace(',', ''))

# 236
def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

# 237
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)

# 238
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

# 239
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)

# 240
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
# 226
def print_5xn(line):
    count_num = int(len(line) / 5)
    for x in range(count_num + 1) :
        print(line[x * 5: x * 5 + 5])
print_5xn("아이엠어보이유알어걸")

# 227
def print_mxn(line, num):
    chunk_num = int(len(line) / num)
    for x in range(chunk_num + 1) :
        print(line[x * num: x * num + num])
print_mxn("아이엠어보이유알어걸", 3)

def make_url(string) :
    url = "www." + string + ".com"
    return url
make_url("naver")




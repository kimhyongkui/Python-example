#71
my_variable = ()
print(type(my_variable))

#72
movie_rank = ("닥터스트레인지", "스플릿", "럭키")
print(movie_rank)

#73
my_tuple = (1)
print(type(my_tuple))
#하나의 정숫값을 저장하면 튜플로 정의되지 않는다 -> type(my_tuple) -> int
#따라서 하나의 데이터가 저장되는 경우, 다음과 같이 쉼표를 입력해야 한다. my_tuple = (1, )
my_tuple = (1, )
print(type(my_tuple))

#74
#튜플은 원소의 값을 변경할 수 없다

#75
t = 1, 2, 3, 4
print(type(t))
# 원칙적으론 튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해 괄호 없이도 동작함.

#76
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
#새로운 튜플을 만들어야함. 기존 튜플은 자동삭제됨

#77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest_data = list(interest)
print(type(interest_data))

#78
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest1 = tuple(interest)
print(type(interest1))

#79
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

#80
range(2, 99, 2)
a = range(2, 99, 2)
print(tuple(a))

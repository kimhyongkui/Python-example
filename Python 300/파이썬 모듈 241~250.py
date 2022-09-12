# # 241
# import datetime
#
# now = datetime.datetime.now()
# print(now)
#
# # 242
# import datetime
#
# now = datetime.datetime.now()
# print(now, type(now))
#
# # 243
# import datetime
#
# now = datetime.datetime.now()
#
# for day in range(5, 0, -1):
#     delta = datetime.timedelta(days=day)
#     date = now - delta
#     print(date)
#
# # 244
# import datetime
#
# now = datetime.datetime.now()
# print(now.strftime("%H:%M:%S"))
#
# # 245
# import datetime
#
# day = "2020-05-04"
# ret = datetime.datetime.strptime(day, "%Y-%m-%d")
# print(ret, type(ret))
#
# # 246
# import time
# import datetime
#
# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)
#
# # 247
#
# # 248
# import os
# ret = os.getcwd()
# print(ret, type(ret))
#
# # 249
# import os
# os.rename(#파일주소)

# # 250
# import numpy
# for i in numpy.arange(0, 5, 0.1):
#     print(i)

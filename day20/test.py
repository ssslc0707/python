import collections
import os
import random
import datetime
# values = [1,2,3,4,5,6,7,8,9]
# #
# # defaultdict = collections.defaultdict(list)
# #
# # for i in values:
# #     if i>6:
# #         defaultdict['k1'].append(i)
# #     else:
# #         defaultdict['k2'].append(i)
# #
# # print(defaultdict)
import sys
import time

# print(1 // 10)
# def getCode(num):
#
#     code = ''
#
#     for i in range(num):
#         randint = random.randint(1, 92)
#
#         c = chr(randint) if randint > 64 else randint
#
#         code = code + str(c)
#     return code
#
#
# print()
# #print(time.time(time.strptime()) - time.time())
# print((datetime.datetime.strptime('2018-12-06 19:45:24','%Y-%m-%d %H:%M:%S')-
#        datetime.datetime.strptime('2018-12-05 19:45:24','%Y-%m-%d %H:%M:%S')))
#
# print(datetime.datetime.strptime('2018-12-06 19:45:24','%Y-%m-%d %H:%M:%S').timestamp())
#
# def getTwoTime(startTime,endTime):
#     startTime = time.mktime(time.strptime(startTime, '%Y-%m-%d %H:%M:%S'))
#     endTime = time.mktime(time.strptime(endTime, '%Y-%m-%d %H:%M:%S'))
#     return endTime - startTime
#
# print(getTwoTime('2018-12-06 19:45:24','2018-12-07 19:45:24')//(60*60))
#
# print(os.path.abspath('test.py'))

print(sys.argv)

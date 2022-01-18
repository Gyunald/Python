# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# import glob
# print(glob.glob("*.py"))

# import os
# print(os.getcwd())

# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder) # 폴더 삭제
#     print(folder, "폴더를 삭제하였습니다.")
# else :
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())

import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print(datetime.date.today())
today = datetime.date.today()
td = datetime.timedelta(days=100)
print(today + td)
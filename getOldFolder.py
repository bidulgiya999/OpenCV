# 날짜 시간 형태로 폴더를 생성하고
# 가장 오래된 폴더 정렬해서 찾기, 지우기

import os
#import datetime
from datetime import datetime

# 폴더를 생성
# 현재 폴더 아래에 test 폴더를 생성
# test 폴더 아래에 날짜_시간 폴더를 생성

#basePath = "test/A/B" # 폴더가 만들어짐, 한번더실행하면 이 파일이 존재해서 파일을 만들수 없다고함
basePath = "test"
# 폴더 만드는 함수
os.makedirs(basePath, exist_ok = True) # True라면 원래 파일이 있어도 만들어짐

# 현재시간 가져오기
#now = datetime.datetime.now() #import datetime

now = datetime.now() # from datetime import datetime

# 폴더명을 "20240904_11"
#folderName = now.strftime("%Y%m%d_%H")

for hour in range(24):
    folderName = now.strftime("%Y%m%d_")
    folderName = folderName + str(hour)
    #print(folderName) # 이게 실행되면 폴더는 아직 만들어지지않고 문자열만 만들어진것
    folderName = os.path.join(basePath, folderName)
    #print(folderName)
    os.makedirs(folderName, exist_ok=True) # 이걸 통해서 폴더를 만들 수 있다



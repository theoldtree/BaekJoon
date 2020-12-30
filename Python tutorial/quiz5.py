### 난수 매칭하기
# 택시기사 1 ~ 50 명의 승객과 매칭
# 승객별 운행 소요시간은 5분 ~ 50분
# 나는 5분 ~ 15분 사이의 승객만 탑승을 시켜야 합니다.

from random import *
cnt = 0
for i in range (1,51):
    time = randrange(5,51) # **해당하는 범위 내의 정수 랜덤으로 선정**
    if 5 <= time <=15:
        print("[0] {0}번째 손님 (소유시간 : {1}분)".format(i,time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))

print("총 탐승 승객 : {0}분".format(cnt))


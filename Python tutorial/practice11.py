### 전역변수 global

gun = 10

def checkpoint(soldiers):
    global gun # 전역 변수를 쓰겟다는 의미의 global
    gun = gun - soldiers
    print("remaining gun : {0}".format(gun))

def checkpoing_ret(gun, soldiers):
    gun = gun-soldiers
    print("remaining gun : {0}".format(gun))

print("total gun : %d",gun)
checkpoint(2)
checkpoing_ret(gun,2)
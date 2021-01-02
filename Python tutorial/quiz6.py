# 표준 체중을 구하는 프로그램
# 표준체중 :
#  - 남자 : 키 * 키 * 22
#  - 여자 : 키 * 키 * 21

# 표준체중은 함수 내에서 계산
#  - 함수명 : std_weight
#  - parameter : height, sex

# 표준 체중은 소수점 둘째 자리 까지 표시

def std_weight(height,sex):
    height = height/100
    if(sex == "man"):
        return round((pow(height,2))*22,2)
    elif(sex == "woman"):
        return round((pow(height,2))*21,2)

height = 175
sex = "woman"
std = std_weight(height,sex)
print("standard wieght of a {2} whose height is {0} is {1}".format(height,std,sex))
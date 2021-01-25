###표준 입출력
import sys
print("python","java","js",sep=" vs ") # sep 으로 , 사이사이에 들어갈 것을 지정해줄수 있음
print("python","java","js",file=sys.stdout)
print("python","java","js",file=sys.stderr)

scores = {"eng":0, "math": 30, "coding": 50}
# dic.keys : key list
# dic.values : value list
# dic.items : key,value 튜플 list
for subject, score in scores.items(): # dictionary 에 있는 key 와 value를 쌍으로 리턴할수 있음
    print(subject.ljust(8),str(score).rjust(4), sep = ":") # ljust rjust 왼쪽정렬 오른쪽정렬

for number in range(1,21):
    print("waiting num : " + str(number).zfill(3)) # 3카능로 정렬하는데 빈공간은 0으로 채움

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일땐 + 음수일땐 - 표시
print("{0: >+10}".format(-500))
print("{0: >+10}".format(+500))
# 왼쪽 정렬하고, 빈칸으로 _ 채움
print("{0:_<10}".format(50))
# 3자리 마다 , 를 찍어줌
print("{0:,}".format(100000000000))
# 3자리 마다 , 를 찍어주고 부호도 표시
print("{0:+,}".format(100000000000))
print("{0:-,}".format(-100000000000))
# 20자리 공간 확보, 빈 공간은 ^ 로 채우고, 부호표시를 하고, 3자리 마다,찍어주기
print("{0:^<+20,}".format(100000000000))

# 소수점 출력
print(5/3)
# 소수점 6째 자리 까지 표시
print("{0:f}".format(5/3))
# 소수점 2째 자리 까지 표시
print("{0:.2f}".format(5/3))


answer = input("input value : ") # 괄호 안에 내용이 출력되고 입력을 기다림 -> 문자열 형태로 입력받음
print("vlaue is {0}".format(answer))
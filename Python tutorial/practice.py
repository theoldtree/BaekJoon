print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
print('풍선')
print("나비")   # '' "" 모두 문자열에 이용된다.
print(True)
print(10>5)
print(not True)
print(not (5>10))

print(2**3) # n제곱 연산
print(5%3)
print(5/3) # 나눈결과 소수점까지 출력됨
print(5//3) # 몫구하기
print(3+4 == 7)
print((3>0) and (3<5)) # and 연산, or 도 마찬가지
print((3>0) & (5>0)) # &을 한번만 쓴다. or 도 마찬가지

animal = "dog"
name = "Mike"
age = 4
hobby = "walking"
is_adult = (age >= 3)

print("Our family " + animal + " name is " + name)
print("his hobby is " + hobby + " and age is " + str(age)) # +와 str을 같이 쓸경우 나머지 자료형에 대해서 str형으로 형변환시켜줘야함
print("his hobby is",hobby, "and age is",age) # , 로 + 을 대채할 수 있음. 띄어쓰기가 포함된다.
print("is he a adult or not? " + str(is_adult))

number = 2 + 3 * 4
print(number)
number /= 2
print(number)
number += 2
print(number)
number %= 5
print(number)
number -= 2
print(number)

print(abs(-5)) # 절대값 계산
print(pow(2,10)) # n 제곱 계산
print(max(5,12)) # 최대값 계산
print(round(3.5)) # 반 올림값 계산

from math import * # 수학용 라이브러리 floor ceil sqrt이 정의되어 있음
print(floor(3.15)) # 내림 계산
print(ceil(3.15)) # 올림 계산
print(sqrt(7)) # 제곱근 계산

from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(int(random()*10)) # 0 ~ 10 사이의 임의의값 생성
print(int(random()*10)) # 0 ~ 10 사이의 임의의값 생성
print(int(random()*10)) # 0 ~ 10 사이의 임의의값 생성
print(int(random()*10)) # 0 ~ 10 사이의 임의의값 생성
print(int(random()*10)) # 0 ~ 10 사이의 임의의값 생성
print(int(random()*45) +1)
print(int(random()*45) +1)
print(int(random()*45) +1)
print(int(random()*45) +1)
print(int(random()*45) +1)
print(int(random()*45) +1)
print(randrange(1,46)) # 1 ~ 46 미만의 임의의값 생성
print(randint(1,46)) # 1이상 46이하의 임의의 값 생성
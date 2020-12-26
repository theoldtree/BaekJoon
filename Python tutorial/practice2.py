sentence = 'I`m a boy'
print(sentence)
sentence2 = "python is easy"
print(sentence2)
sentence3 = """
i'm a girl
python is hard
""" # """ """ 여러줄 입력
print(sentence3)

### 문자열 관련 함수 ###
idnumber = "970316-1234567"
print('sex',idnumber[7])
print('year',idnumber[0:2]) # 0~1index 값 출력
print('month',idnumber[2:4])
print('day',idnumber[4:6])
print('birth',idnumber[:6]) # 처음부터 6자리 전까지
print('after number',idnumber[7:]) # 7번자리부터 끝까지
print('after number',idnumber[-7:]) # 뒤의 7자리부터 끝까지

python = "Python is Amazing"
print(python.lower()) # 소문자로 변경
print(python.upper()) # 대문자로 변경
print(python[0].isupper()) # 첫번째 글자가 대문자인지 검사
print(len(python)) # 문자열의 길이를 반환
print(python.replace("Python",'Java')) # 문자열에서 해당 문자를 찾은뒤 바꿔서 출력

index = python.index('n') # 해당문자가 첫번째로 나오는 위치를 출력
print(index)
index = python.index('n',index+1) # 뒤의 나온는 argument 부터 찾아서 출력
print(index)
print(python.find('n')) # 만약 찾는 문자가 없으면 -1을 반환함, index로 쓴다면 오류를 출력
# print(python.index('java')) # 에러를 출력
print(3)


### 여러가지 출력 형식 ###
print("i am %d year old" %20) # 숫자 insert시 %d를 이용 ,는 따로    쓰지 않음
print("my hobby is %s" %"python coding") # 문자열 insert시 %s 사용
print('Apple is start with letter %c' %"A")
print("I like color %s and %s" %("blue", "red")) # 여러개를 출력하고 싶을때 %(,,)

print('my age is {}'.format(24))
print('my favorite fruits are {} and {}'.format("banana", "watermelon"))
print('my favorite fruits are {1} and {0}'.format("banana", "watermelon")) # 위치 바꿈 순번에 맞게 출력이 가능


print("i'm {age} years old, and i like {color} color.".format(age=20,color="red")) # 변수 이름을 지정하여 출력
print("i'm {age} years old, and i like {color} color.".format(color="red",age=20)) # 순서에 관계없이 해당위치에 들어감


age = 20
color = "red"
print(f"i am {age} years old and i like {color} color")
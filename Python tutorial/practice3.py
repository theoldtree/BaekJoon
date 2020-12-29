print("hardeer better \nfaster stronger")
print("i am \"sam\"") # ""문장안에 ""의 기호를 삽입하고 싶을 때
print("filePath : user\\desktop\\yjeognmu") # 문장내에서 \를 표시하고 싶을 때


### 리스트
subway = [10, 20, 30]
print(subway)

subway2 = ["mike", "sam", "jason"]
print(subway2)

print(subway2.index("sam"))

subway2.append("haha") # 리스트 뒤에 추가
print(subway2)

subway2.insert(1,"jenny") # 리스트 사이에 삽입할때
print(subway2)

subway2.append("mike")
print(subway2.count('mike'))

print(subway2.pop()) # 한명씩 뒤에서 꺼냄
print(subway2)
print(subway2.pop())
print(subway2)
print(subway2.pop())
print(subway2)

num_list = [3,2,4,5,1]
num_list.sort() # 리스트의 정렬
print(num_list)
num_list.reverse() # 리스트를 역으로 정렬
print(num_list)
num_list.clear() # 리스트 내의 모든 항목을 삭제
print(num_list)

mixed_list = ["sam",1,'30',True] # 리스트에는 여러가지 자료형이 올 수 있음
print(mixed_list)

subway.extend(subway2) # subway에  sunway2 리스트를 합쳐줌
print(subway)
print(subway[0]) # subway에 index 0 에 있는 값을 출력할 수 있음
### 사전
cabinet = {3:'mike', 100:'jasnon'}
print(cabinet)
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))

# print(cabinet[5]) 지정이 안된 key값을 원할경우 에러가 나며 프로그램이 자동으로 종료됨
print(cabinet.get(5)) # 지정이 안된 key값을 원할경우 None이 출력됨
print(cabinet.get(5,"available")) # 지정이 되어 있으면 value 값이 출력이 되고, 만약 없으면 , 뒤의 내용이 출력됨

print(3 in cabinet) # in key워드 값
print(5 in cabinet)

cabinet2 = {"a-3":"jenny", "b-100":"julia"}
print(cabinet2["a-3"])
print(cabinet2["b-100"])

cabinet2["c-30"] = "lisa" # 만약 key값이 있으면 값이 업데이트가 되고 만약 없는 값이면 새로운 값이 추가가됨

del cabinet2["a-3"] # 사전안에 원하는 key를 삭제할 수 있음
print(cabinet2)

print(cabinet2.keys()) # key 값들을 출력할 수 있음
print(cabinet2.values()) # value 값들을 출력할 수 있음
print(cabinet2.items()) # key와 value 값들을 출력 할 수 있음
cabinet2.clear()
print(cabinet2)
### 집합
my_set = {1,2,3,3,3} # 사전에서와 형식이 다름
my_set = set([1,2,3,3,3]) # 사전을 만드는 다른 형식
print(my_set) # 중복된 값은 제외되고 저장이 됨

java_dev = {"mike", "jason", "chriss", "jennifer"}
python_dev = {"elisa", "marz", "mike", "jason"}
print(java_dev & python_dev) # 교집합을 구하고 싶을 때 
print(java_dev.intersection(python_dev)) # 교집합을 구하는 다른 형식
print(java_dev | python_dev) # 합집합을 구하고 싶을 때
print(java_dev.union(python_dev)) # 합집합을 구하는 다른 방식
print(java_dev - python_dev) # 차집합을 구하고 싶을 때
print(java_dev.difference(python_dev)) # 차집합을 구하는 다른 방식
python_dev.add("taehee") # 추가 할 때 
print(python_dev)
java_dev.remove("mike") # 제거하고 싶을 떄
print(java_dev)
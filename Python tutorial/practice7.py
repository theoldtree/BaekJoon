### 자료구조의 변경
menu = {"coffe", "milk", "milk"}
print(menu,type(menu)) # type을 확인 하고 싶을 때 

menu = list(menu) # 리스트로 변경
print(menu,type(menu))

menu = set(menu)
print(menu, type(menu))
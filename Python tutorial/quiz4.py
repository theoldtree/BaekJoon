### 댓글 추첨 어플 (1~20명중 4명을 추첨)
# 무작위 추첨이되 중복은 불가
# 추첨을 통해 1명은 치킨 3명은 커피쿠폰을 받게 됨


from random import *
lst = range(1,21) # 1부터 20까지 range형 자료형을 만드는 함수
print(type(lst))
lst = list(lst)
print(type(lst))
lst_selected = sample(lst,4) # 리스트에 있는 것을 무작위로 뽑아 다시 리스트로 만듦
print(lst_selected)
shuffle(lst_selected) # 리스트의 내용을 무작위로 셔플함
print(lst_selected)

print("---- Winner! ----")
print("chicken winner :",lst_selected[0])
print("coffee winner :",lst_selected[1:])
print("---- Lucky! ----")

num1, num2 = input().split(" ")
num1 = (int(num1))
num2 = (int(num2))
bool_num = num1 & num2
if not(bool_num):
    print(0)
else:
    print(1)

# 모범 답안
num1,num2=input().split()
num1=int(num1)
num2=int(num2)
b1=bool(num1)
b2=bool(num2)
bool_num=int(b1 and b2)
print(bool_num)
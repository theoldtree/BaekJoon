# num1 = input()
# num1 = int(num1)
# num2 = input().split(" ")
# num2.reverse() # TODO 따로 변수를 지정하지 않아도 리스트 안에서 그대로 역으로 저장됨
# for index in range(0,num1):
#     value = int(num2[index])
#     print(value, end = " ")

arr=[]
a=input()
b=input().split()

n=int(a)
for i in range(n) :
    arr.append(int(b[i]))

i=n-1
while i>=0 :
    print(arr[i], end=' ')
    i-=1
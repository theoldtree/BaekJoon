num1, num2, num3, num4 = input().split(" ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = int(num4)
for index in range(0,num4-1):
    num1 = num1*num2+num3
print(num1)
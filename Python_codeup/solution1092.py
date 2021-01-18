num1, num2, num3 = input().split(" ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
count = 1
while count%num1 != 0 or count%num2 != 0 or count%num3 != 0:
    count += 1
print(count)
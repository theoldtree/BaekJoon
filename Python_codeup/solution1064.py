num1, num2, num3 = input().split(" ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
if num1 < num2:
    small = num1
else : 
    small = num2
print(small) if small < num3 else print(num3)

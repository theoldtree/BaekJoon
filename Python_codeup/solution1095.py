num1 = input()
num1 = int(num1)
num2 = input().split(" ")
small = int(num2[0])
for index in range(0,num1):
    value = int(num2[index])
    if value < small:
        small = value

print(small)

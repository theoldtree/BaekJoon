num1, num2, num3 = input().split(" ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
count = num1 * num2 * num3
for index1 in range(0,num1):
    for index2 in range(0,num2):
        for index3 in range(0,num3):
            print("{} {} {}".format(index1, index2, index3))
print(count)
num1, num2 = input().split(" ")
num1 = int(num1)
num2 = int(num2)
for dice1 in range(1,num1+1):
    for dice2 in range(1, num2 +1):
        print("{} {}".format(dice1,dice2))
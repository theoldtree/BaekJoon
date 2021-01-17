num = input()
num = int(num)
sum = 0
for count in range(0,num):
    sum += count
    if num <= sum:
        print(count)
        break
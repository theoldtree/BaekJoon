num = input()
num = int(num)
sum = 0
index = 1
while True:
    sum += index
    index += 1
    if num <= sum:
        break
print(sum)
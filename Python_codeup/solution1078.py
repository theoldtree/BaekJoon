num = input()
num = int(num)
sum = 0
for count in range(0,num+1):
    if count % 2 == 0:
        sum += count
print(sum)
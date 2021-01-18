num = input()
num = int(num)
for index in range(1,num+1):
    if index % 3 == 0:
        continue
    print(index,end=" ")
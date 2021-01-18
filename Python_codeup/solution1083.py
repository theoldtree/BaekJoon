num = input()
num = int(num)
for index in range(1,num+1):
    if index % 3 == 0:
        print("X",end=" ")
    else :
        print(index,end=" ")
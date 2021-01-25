h,w = map(int,input().split(" "))
matrix = [[0 for col in range(w)] for row in range(h)]
count = int(input())
for index in range(count):
    l,d,x,y = map(int,input().split(" "))
    if d == 0:
        for row in range(l):
            matrix[x-1][y-1+row] = 1
    else:
        for col in range(l):
            matrix[x-1+col][y-1] = 1
for row in range(len(matrix)):       
    for col in range(len(matrix[row])):
        print(int(matrix[row][col]), end=' ')
    print()
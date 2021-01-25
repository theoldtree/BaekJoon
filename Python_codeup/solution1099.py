matrix = []
for index in range(10):
    struct_list = list(map(int,input().split()))
    # TODO 배열 = 리스트 -> 배열에 추가할때 list의 형태로 전환해줘야 한다.
    matrix.append(struct_list) 
row, col = 1,1
while True:
    if row > 9 or col > 9:
        break
    if matrix[row][col] == 2:
        matrix[row][col] = 9
        break
    elif matrix[row][col] == 0:
        matrix[row][col] = 9
    if (matrix[row][col+1] == 0) or (matrix[row][col+1] == 2):
        col += 1
        continue
    elif (matrix[row][col+1] == 1):
        row += 1
        continue

for row in range(len(matrix)):       
    for col in range(len(matrix[row])):
        print(int(matrix[row][col]), end=' ')
    print()
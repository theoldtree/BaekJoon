matrix = []
for index in range(10):
    struct_list = list(map(int,input().split()))
    # TODO 배열 = 리스트 -> 배열에 추가할때 list의 형태로 전환해줘야 함
    # 숫자 관련해서 다룰띠는 int로 전환해주는거 있지 않기
    # map을 사용하여 리스트안의 내용물을 하나하나 다룰수 있음
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
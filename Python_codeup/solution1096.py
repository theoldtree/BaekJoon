matrix = [[0 for col in range(19)] for row in range(19)]
# TODO 2차원 배열의 초기화
num1 = input()
num1 = int(num1)
for point in range(num1):
    point = input()
    (x,y) = tuple(point.split(" "))
    x = int(x)
    y = int(y)
    matrix[x-1][y-1] = 1

for row in range(len(matrix)):            
    for col in range(len(matrix[row])):   
        print(matrix[row][col], end=' ')
        # TODO 2차원 배열의 출력
    print()
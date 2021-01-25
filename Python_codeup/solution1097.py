matrix = []
for index in range(19):
    num_list = list(map(int,input().split(" ")))
    matrix.append(num_list)
    # TODO map을 이용하여 인자들을 int로 수정가능 
    # TODO map을 썻다면 다시 형변환을 시켜줘야 한다
    # TODO 입력값이 문자열이므로 숫자와 관련된 함수를 짜려면 int형으로 모두 바꿔줘야됨
count = input()
count = int(count)
for index in range(count):
    x, y = map(int, input().split())
    for i in range(19): 
        if matrix[x-1][i] == 1: 
            matrix[x-1][i] = 0 
        else:
            matrix[x-1][i] = 1 
        if matrix[i][y-1] == 1: 
            matrix[i][y-1] = 0 
        else: 
            matrix[i][y-1] = 1
for row in range(len(matrix)):       
    for col in range(len(matrix[row])):
        print(int(matrix[row][col]), end=' ')
        # TODO 2차원 배열의 출력
    print()


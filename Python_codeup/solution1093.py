count = input()
num_list = input().split(" ")
dic = dict()
num = 0
for index in range(1,24):
    index = int(index)
    dic[index] = 0 # TODO dictionary 에서의 단어 추가
for index in range(0,count):
    num = int(num_list[index])
    if num in dic:
        dic[num] = dic[num] + 1
print(dic)
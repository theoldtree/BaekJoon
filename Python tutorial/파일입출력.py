### 파일 입출력
# 파일 출력
score_file = open("score.txt","w",encoding="utf8")
print("math : 0", file = score_file)
print("english : 50", file = score_file)
score_file.close()

score_file = open("score.txt","a",encoding="utf8")
score_file.write("sciece : 80")
score_file.write("\ncoding : 50")
score_file.close()

# 파일 입력
score_file = open("score.txt","r",encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline(),end="") # 줄별로 파일을 읽음
print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline())
score_file.close()

score_file = open("score.txt","r",encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line,end="")
print()
score_file.close()

score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines() # 파일을 읽어서 리스트 형태로 저장
for line in lines:
    print(line,end="")
score_file.close()
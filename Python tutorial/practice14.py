### 피클
import pickle
profile_file = open("profile.pickle","wb")
profile = {"name":"park", "age":30, "hobby":["soccer","golf","swimming"]}
print(profile)
pickle.dump(profile,profile_file) # profile 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file) # 파일에 있는 정보를 profile 에 저장
print(type(profile))
print(profile)
profile_file.close()

### with
import pickle
with open("profile.pickle","rb") as profile_file: # with로 파일을 열었을 시 자동으로 파일을 close해줌
    print(pickle.load(profile_file))

with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("i'm studying python very hard")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())

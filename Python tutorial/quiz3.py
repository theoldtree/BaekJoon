### 페이지의 비밀번호를 생성하라!
# 규칙1 : 도메인 주소 이후로만 출력
# 규칙2 : . 이후로는 주소를 생략
# 규칙3 : 완성된 암호 -> 규칙2로 만들어진 앞 세글자 + 규칙2의 글자길이 + 규칙2내의 e의 갯수 + !
page = "http://google.com"

rule1 = page.replace("http://","") # 꿀팁! : 특정 문자를 제거할때 replace(string,"")
rule2_index = rule1.index(".")
rule2 = rule1[:rule2_index]
rule2_len = len(rule2)
rule3_front = rule2[:3]
count_e = rule2.count("e") # 문장내에 특정 문자열의 갯수를 count할 수 있음.
password = rule3_front + str(rule2_len) + str(count_e)+ "!"
print("password of the site {url} is {password}".format(password = password, url = page))
print("password of the site {1} is {0}".format(password, page))
print("password of the site {} is {}".format(page,password))
print(f"password of the site {page} is {password}")
print("password of the site %s is %s" %(page,password))

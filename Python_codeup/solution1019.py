year,month,day = input().split(".")
year = int(year)
month = int(month)
day = int(day)
print("%04d.%02d.%02d" %(year,month,day))

 # 0과 숫자의 조합으로 원하는 길이로 출력하고 나머지는 0으로 채우기
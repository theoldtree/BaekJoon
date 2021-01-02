# 당신의 회사는 매주 1회 작성해야 하는 보고서가 있다.
# 보고서는 다음과 같은 형식이어야 한다.

# - x 주차 주간보고 -
# 부서 : 
# 이름 :
# 업무 요약 : 

# 1주차 부터 3주차까지의 보고서를 만드는 프로그램을 적성하시오. 파일명은 'x주차.txt'와 같은 형식이 되어야 합니다.

for week in range(1,4):
    with open(str(week) + "week report".format(week),"w",encoding="utf8") as report_file:
        report_file.write("- {0} week report -".format(week))
        report_file.write("\ndepartment: ")
        report_file.write("\nname: ")
        report_file.write("\nsummary: ")

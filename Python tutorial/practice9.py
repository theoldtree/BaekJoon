### 반복문
# print("waiting number : 1")
# print("waiting number : 2")
# print("waiting number : 3")
# print("waiting number : 4")

## for
for waiting_no in list(range(0,5)):
    print("waiting nuber : {0}".format(waiting_no))

avengers = ["ironman", "spiderman", "batman", "hokeye"]
for hero in avengers:
    print("you are a good main {}!".format(hero))


## while
customer = "mike"
index = 5
while(index >=1):
    print("{0}'s coffee is ready! {1} is left".format(customer, index))
    index-=1
    if index == 0:
        print("nothing left")

customer2 = "thor"
person = "unknown"
# while person != customer2:
#     print("{0} coffee is ready".format(customer2))
#     person = input("who r you? ")


## continue break
absent = [2, 5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("stop")
        break
    print("{} reades a book".format(student))


students = list(range(1,6))
print(students)
students = [i+100 for i in students] # for 문을 사용하는 방법 2
print(students)

students = ["Iron man", "Thor", "i'm groot"]
students_to_cap = [i.upper() for i in students]
print(students_to_cap)
students_name_len = [len(i) for i in students]
print(students_name_len)
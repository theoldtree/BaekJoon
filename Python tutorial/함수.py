### 함수
def open_account():
    print("new account was opened")

open_account()

def deposit(balance, money):
    print("money was in, left money is {0}".format(balance+money))
    return balance+money

def withdraw(balance, money):
    if balance > money:
        print("withdrawable, balance is {0}".format(balance-money))
        return balance-money
    else:
        print("withdraw isn't able, balance is {0}".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return (commission, balance-money-commission)
    # TODO 튜플형식으로 두개 이상 리턴 할 수 있음

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 200)
print("commission is {0}, balance is {1}".format(commission, balance))

## 기본값 설정(default 값)
def  profile(name, age, main_lang):
    print("name : {0}, age : {1}, main_language : {2}".format(name, age, main_lang))
def  profile(name, age=17, main_lang="python"):
    print("name : {0}, age : {1}, main_language : {2}".format(name, age, main_lang))

profile("mike",20,"python")
profile("jenny",21,"java")
profile("sunny")
profile("jane")
profile(name="jessy", main_lang="python", age=20) # 변수를 직접 지정해주면 순서가 바뀌어도 무관

## 가변인자
def profile(name, age, *language): # TODO *로 많은 인자를 전달 받을 수 있음
    print("name : {0}, age : {1}".format(name, age), end = "  ") # 개행을 하고싶지 않을때 -> end
    for lang in language:
        print(lang, end = " ")
    print()

profile("johnyy",20,"python","java","c","c++","js","ts","c++")
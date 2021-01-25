### 예외처리
## try-catch
try:
    print("calculator for dividing")
    num1 = int(input("input : "))
    num2 = int(input("input : "))
    print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
except ValueError: # catch
    print("Error! you inputed worng format")
except ZeroDivisionError as err:
    print(err)
    print("you can't divide num by zero")
except Exception as err: # 모든 예외 처리
    print(err)
    print("something went wrong")

## 예외 만들기
class BigNumberException(Exception): # Exception class를 상속해준다
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg
    pass

## throw
try:
    print("dividor for num 0~9")
    num1 = int(input("input : "))
    num2 = int(input("input : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberException("input value {0} : {1}".format(num1,num2)) # throw
    print("{0}/{1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError: # catch
    print("you inputed wrong num, please input number range in 0~9")
except BigNumberException as err:
    print("big number exception was errupted")
    print(err)
finally: # finally 예외가 발생하든 발생하지 않든 무조건 실행되는 부분
    print("thanks for using calc")


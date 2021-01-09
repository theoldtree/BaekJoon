class NegativeNumError(Exception):
    pass

def price(people):
    try:
        if people < 0:
            raise NegativeNumError
        print("the price of {0} is {1}".format(people, people * 10000))

    except NegativeNumError:
        print("please input number at least 0")

def price_morning(people):
    try:
        if people < 0:
            raise NegativeNumError    
        print("the price_morning of {0} is {1}".format(people, people * 8000))
    except NegativeNumError:
        print("please input number at least 0")
           
def price_soldier(people):
    try:
        if people < 0:
            raise NegativeNumError    
        print("the price_soldier of {0} is {1}".format(people, people * 8000))
    except NegativeNumError:
        print("please input number at least 0")



num = input()
num = int(num)
if num > 0:
    print("plus")
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
else:
    print("minus")
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
    
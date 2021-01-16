num = input()
length = len(num)
amount_num = 10**length/10
for index in range(0,length):
    print("["+str(int(num[index])*int(amount_num))+"]")
    amount_num /= 10
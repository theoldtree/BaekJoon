hex_num = input()
hex_num = int("0x" + hex_num,16)
res = 0
for index in range(1,16):
    res = index * hex_num
    print("{}*{}={}".format(hex(hex_num)[2:].upper(),hex(index)[2:].upper(),hex(res)[2:].upper()))
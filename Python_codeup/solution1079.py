char_list = input().split(" ")
for char in char_list:
    if char == 'q':
        print("q")
        break
    print(char)
    
    # TODO print("{0}".format(char),end="") : 같은 줄에 출력하고 싶을때
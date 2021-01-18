r, g, b = input().split(" ")
r = int(r)
g = int(g)
b = int(b)
size =r*g*b/8/1024/1024
print("%0.2f" %size, end=" ")
print("MB")
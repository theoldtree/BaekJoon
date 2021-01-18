h, b, c, s = input().split(" ")
h = int(h)
b = int(b)
c = int(c)
s = int(s)
size = h*b*s*c/8/1024/1024
print("%0.1f" %size,end=" ")
print("MB")

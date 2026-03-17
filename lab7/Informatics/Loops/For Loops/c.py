import math
a = int(input())
b = int(input())
start = math.ceil(math.sqrt(a))

x = start
while x * x <= b:
    print(x * x, end=' ')
    x += 1
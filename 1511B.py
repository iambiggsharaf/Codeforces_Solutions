import math

t = int(input())
for i in range(t):
    a, b, c = [int(j) for j in input().split()]
    x = (10 ** (a - 1))
    y = (10 ** (b - 1))
    z = 5
    z = z * (10 ** (c - 1))
    print(x, y + z)


    # first = min(x, y)
    # second = max(x, y)
    # flag = False
    # w = (first + 1) // 10
    # q = (second + 1) // 10
    # print(w, q)
    
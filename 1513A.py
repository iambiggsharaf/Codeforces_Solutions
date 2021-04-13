t = int(input())
for i in range(t):
    a, b = [int(x) for x in input().split()]
    if b > (a - 1) // 2:
        print(-1)
    else:
        foo = []
        for j in range(1, a + 1):
            foo.append(j)
        q = 1
        for j in range(b):
            foo[q] += 1
            foo[q + 1] -= 1
            q += 2
        for t in foo:
            print(t, end = " ")
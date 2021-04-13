t = int(input())
for i in range(t):
    n = int(input())
    foo = [int(j) for j in input().split()]
    # print(foo)
    flag = False
    for i in range(1, n - 1):
        if foo[i] != foo[i - 1] and foo[i] != foo[i + 1]:
            print(i + 1)
            flag = True
    if flag == False:
        if foo[0] != foo[1]:
            print(1)
        if foo[n - 1] != foo[n - 2]:
            print(n)
    
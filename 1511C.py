a = input()
foo = [int(i) for i in input().split()]
bar = [int(i) for i in input().split()]
for i in bar:
    indexx = foo.index(i)
    print(indexx + 1, end = " ")
    ans = foo[indexx]
    foo[1: indexx + 1] = foo[ : indexx]
    foo[0] = ans

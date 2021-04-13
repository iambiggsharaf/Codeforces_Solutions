from typing import Counter


t = int(input())

for i in range(t):
    n = int(input())
    foo = [int(j) for j in input().split()]
    print(foo.count(1) + foo.count(3))
#!/bin/python3
import sys,os
from collections import *
# kevinsogo
for cas in range(int(input())):
    n, m, k = map(int, input().split())
    ans = 0
    f = defaultdict(int)
    p = k
    f[p * k % m] += 1
    for v in map(int, input().split()):
        v %= m
        if v == 0:
            f.clear()
            p = k
        else:
            p = p * v % m
            ans += f[p]
        f[p * k % m] += 1
    print(ans if k else n * (n + 1) // 2 - ans)
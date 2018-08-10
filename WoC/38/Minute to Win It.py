#!/bin/python3

import os,sys
from collections import *
input = sys.stdin.readline

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N,K = map(int,input().strip().split())
    A=map(lambda s:int(s[1])-K*s[0],enumerate(input().strip().split()))
    C=Counter(A)
    res = N-max(C.values())

    fptr.write(str(res) + '\n')

    fptr.close()
#!/bin/python3
import sys,copy
from collections import *
from itertools import *
from functools import lru_cache
from operator import sub
from heapq import *
from sys import stdin
input = stdin.readline
#sys.stdin = open('G:\hackerrank\WoC\\34\\3. Same Occurrence\\t1.txt', 'r')

N, Q = map(int, input().strip().split())
A    = list(map(int, input().strip().split()))
S    = set(A)
I2A  = tuple(S)
A2I  = { v:i for i,v in enumerate(I2A) }
M = len(A2I)

MPOS = [[] for _ in range(M)]


@lru_cache(None)
def calcY(y):
    res=0
    pos=-1
    for i,v in enumerate(MPOS[y]):
        cnt=v-pos
        res+=cnt*(cnt-1)//2
        pos=v
    cnt=N-pos
    res+=cnt*(cnt-1)//2
    return res

@lru_cache(None)
def calcXY(x,y):
    ix=iy=0
    cntx=cnty=0
    DIFF=defaultdict(int)
    pos=0
    while ix<len(MPOS[x]) and iy<len(MPOS[y]):
        ox,oy=cntx,cnty
        if MPOS[x][ix]<MPOS[y][iy]:
            p=MPOS[x][ix]
            cntx+=1
            ix+=1
        else:
            p=MPOS[y][iy]
            cnty+=1
            iy+=1
        DIFF[ox-oy]+=p-pos
        pos=p
    while ix<len(MPOS[x]):
        p=MPOS[x][ix]
        DIFF[cntx-cnty]+=p-pos
        cntx+=1
        ix+=1
        pos=p
    while iy<len(MPOS[y]):
        p=MPOS[y][iy]
        DIFF[cntx-cnty]+=p-pos
        cnty+=1
        iy+=1
        pos=p

    DIFF[cntx-cnty]+=N-pos
    DIFF[0]+=1
    return sum(map(lambda x:(x*(x-1))//2,DIFF.values()))

def solve():

    for i,a in enumerate(A):
        a=A2I[a]
        A[i]=a
        MPOS[a].append(i)
    
    for _ in range(Q):
        x, y = map(int, input().strip().split())
        x = A2I.get(x, -1)
        y = A2I.get(y, -1)
        x,y  = min(x,y),max(x,y)
        res=0
        xy=(x,y)
        if x==-1 and y==-1:
            res=((N+1)*N)//2
        elif x==y:
            res=((N+1)*N)//2
        elif x==-1:
            res=calcY(y)
        else:
            res=calcXY(x,y)
        print(res)
        
if __name__ == "__main__":
    solve()
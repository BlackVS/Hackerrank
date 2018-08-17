#!/bin/python3
import sys
from collections import *
from itertools import *
from sys import stdin
input = stdin.readline
#sys.stdin = open('G:\hackerrank\WoC\\34\\5. Magic cards\\t0.txt', 'r')

def solve():
    N,M,Q=map(int,input().split())
    CMAX = M*(M+1)*(2*M+1)//6
    maxl = M.bit_length()

    cards=[]
    for _ in range(N):
        ci=map(int,input().split())
        next(ci)
        cards.append( set(c-1 for c in ci) )

    RES = dict()

    for a in range(N):
        mask = 1
        cadrsMasks = [0]*M
        for b in range(a, min(a+maxl, N)):
            allres = [0] * (1<<(b-a+1))
            for card in range(M):
                cardmask = cadrsMasks[card]
                if card in cards[b]:
                    cardmask |= mask
                    cadrsMasks[card] = cardmask
                allres[cardmask] += (card+1)*(card+1)
            res = min(allres)
            RES[a,b] = res
            mask<<= 1

    for _ in range(Q):
        l,r=map(lambda x:int(x)-1,input().split())
        l,r=min(l,r),max(l,r)
        if r-l+1 > maxl:
            print(CMAX)
        else:
            print(CMAX-RES[l,r])

solve()
#!/bin/python3
import sys
from collections import *

input = sys.stdin.readline

YMAX=100000
#NBIAS=1000
KSPLIT=100

class Solution(object):
    def __init__(self):
        #current result
        self.m_accY  = [0]*(1+YMAX)
        #self.m_lines=Counter()
        self.m_Lines=defaultdict(Counter)
        self.m_bias=0
        self.m_bias2=[0,0]

    def addLine(self,k,b):
        b%=k
        if k==1:
            self.m_bias+=1
            return
        if k==2:
            self.m_bias2[b]+=1
            return
        if k>KSPLIT:
            for y in range(b,YMAX,k):
                self.m_accY[y]+=1
            return
        self.m_Lines[k][b]+=1

    def removeLine(self,k,b):
        b%=k
        if k==1:
            self.m_bias-=1
            return
        if k==2:
            self.m_bias2[b]-=1
            return
        if k>KSPLIT:
            for y in range(b,YMAX,k):
                self.m_accY[y]-=1
            return
        self.m_Lines[k][b]-=1

    def query(self,q):
        res=0
        for k,c in self.m_Lines.items():
            v=q%k
            res+=c[v]
        return res+self.m_bias+self.m_bias2[q&1]+self.m_accY[q]

if __name__ == "__main__":
    Q = int(input().strip())
    L = Solution()
    for i in range(Q):
        s=input().strip()
        if s[0]=="+":
            k,b=map(int,s[2:].split())
            L.addLine(k,b)
        elif s[0]=="-":
            k,b=map(int,s[2:].split())
            L.removeLine(k,b)
        else: # ?
            q=int(s[2:])
            r=L.query(q)
            print(r)
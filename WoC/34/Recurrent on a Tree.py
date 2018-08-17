#!/bin/python3
import sys,copy
from collections import *
from itertools import *
from operator import*
from functools import lru_cache
input = sys.stdin.readline
#sys.stdin = open('G:\hackerrank\WoC\\34\\4. Recurrent on tree\\t11.txt', 'r')

MODN=1000000000+7
PIS =2000000016
MAXFS=10

# [a b c d] => [ a b ]
#              [ c d ]
matE = [1, 0, 0, 1];
matF = [1, 1, 1, 0];

def modmod(X):
    for i in range(len(X)):
        if X[i]>=MODN: X[i]%=MODN
    return X

def matadd(A,B):
    return modmod(list(map(add,A,B)))
   

def matdiff(A,B):
    return modmod(list(map(sub,A,B)))

def matmul(A,B):
    C = [ A[0]*B[0]+A[1]*B[2], A[0]*B[1]+A[1]*B[3],
          A[2]*B[0]+A[3]*B[2], A[2]*B[1]+A[3]*B[3] ]
    return modmod(C)

def matmuls(c,A):
    return [ (c*a)%MODN for a in A]

def matprint(M):
    print("{0:3} {1:3}\n{2:3} {3:3}".format(*M))

@lru_cache(None)
def fib(n):
    if n == 0:
        return [1, 0, 0, 1]
    if n>=PIS: 
        n%=PIS
    Y = [1, 0, 0, 1];
    X = [1, 1, 1, 0];
    while n > 1:
        if (n&1)==0: 
            X = matmul(X,X);
        else:
            Y = matmul(X,Y);
            X = matmul(X,X);
        n //= 2;
    return matmul(X,Y)

class Graph(object):
    def __init__(self,n):
        self.VN=n
        self.G = [[] for _ in range(n)]
        self.W = [0]*n
        # DFS
        self.DFS_ans=None

    
    def add_edge(self,x,y):
        self.G[x].append( y )
        self.G[y].append( x )

    def setVWeights(self,itw):
        self.W=tuple(itw)

    def DFS(self,v=0,prev=None):
        if prev==None:
            self.DFS_ans=[0]*4
        G  =self.G
        W  =self.W
        #
        g=fib(W[v])
        msum=[1, 0, 0, 1]
        mres=[1, 0, 0, 1]
        #
        for u in G[v]:
            if u==prev: continue
            mcur=self.DFS(u,v)
            mres=matadd(mres,matmul(msum,mcur))
            msum=matadd(msum,mcur)
        msum=matmul(msum,g)
        self.DFS_ans=matadd(self.DFS_ans,matmul(mres,g))
        return msum

def solve():
    N = int(input())
    G = Graph(N)
            
    for _ in range(N-1):
        a,b=map(int,input().split())
        G.add_edge(a-1,b-1)
    G.setVWeights(map(int,input().split()))

    matres=G.DFS()

    res=G.DFS_ans[0]*2
    for w in G.W:
        res-=fib(w)[0]
        while res<0:
            res+=MODN
    return res%MODN

print(solve()) 
#!/bin/python3
#Little bit faster. Next optimization - maintain diffs instead searching
import sys
from bisect import *
from sys import stdin
input = stdin.readline

class Airports(object):
    def __init__(self,d):
        # sorted by x, freq
        self.X=[]
        self.D=d
        self.minX=None
        self.maxX=None
        #self.dX=[]

    def add(self,x):
        X=self.X
        D=self.D
        if len(X)==0:
            self.minX=self.maxX=x
            self.X.append( x )
            return
        #ptr=bisect_left(X, x)
        #X.insert(ptr, x )
        insort_left(X,x)
        self.minX=min(self.minX, x)
        self.maxX=max(self.maxX, x)
        return

    def check(self):
        X=self.X
        D=self.D
        minX=self.minX
        maxX=self.maxX
        if len(X)<2:
            return 0
        if len(X)==2:
            return D-(maxX-minX)

        # R-L>=D
        res=max(0, D-(maxX-minX))

        dmax=0
        L=maxX-D
        R=minX+D
        xLi=bisect_left(X,L)
        xRi=bisect_right(X,R)
        if maxX-minX<D:
            #don't check L,R itself
            xLi+=1
            xRi-=1
        X=X[xLi:xRi]
        xLi=0
        xRi=len(X)

        if len(X)==0:
            return res
        dmax=max(dmax, X[xLi]-L )
        dmax=max(dmax, R-X[xRi-1])
        for i in range(xLi,xRi-1):
            dmax=max(dmax,X[i+1]-X[i])

        res=max(res,R-L-dmax)
        return res
    
if __name__ == "__main__":
    Q = int(input().strip())
    for _ in range(Q):
        N, D = map(int, input().strip().split(' '))
        ports=Airports(D)
        res =""
        for i,x in enumerate(map(int, input().strip().split(' '))):
            ports.add(x)
            r=ports.check()
            if len(res): 
                res=res+" "
            res+=str(r)
            #print(i,r)
        print(res)
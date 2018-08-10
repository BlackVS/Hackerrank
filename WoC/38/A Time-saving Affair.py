#!/bin/python3
import sys,os
from heapq import *

input = sys.stdin.readline

class Graph(object):
    def __init__(self,n,k):
        self.VN=n
        self.EN=0
        self.TK=K
        self.G       = [[] for _ in range(n)]

    def add_edge(self,x,y,w):
        self.G[x].append( (y,w) )
        self.G[y].append( (x,w) )
        self.EN+=1

    #input : current time
    #output: how long to wait
    def getTWait(self, t):
        i,r=divmod(t, self.TK)
        #i=0,2,4,... - green
        if i&1==0:
            return 0
        return self.TK-r


    def getBestPath(self,s,t):
        VN = self.VN
        EN = self.EN
        G  = self.G
        Q = [(0, s)]
        visited = [False]*VN
        while Q:
            # Always return the list item with min cost.
            (totalCost,u) = heappop(Q)
            wait=self.getTWait(totalCost)
            if not visited[u]:
                visited[u]=True
                if u == t:
                    return totalCost

                for v,w in G[u]:
                    if not visited[v]:
                        heappush(Q, (totalCost+w+wait, v))
        return None

if __name__ == "__main__":
    N = int(input().strip())
    K = int(input().strip())
    M = int(input().strip())
    G=Graph(N,K)
    for _ in range(M):
        u, v, w = map(int,input().strip().split())
        if u!=v:
            G.add_edge(u-1, v-1, w)
    p=G.getBestPath(0,N-1)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #print(p)
    fptr.write(str(p) + '\n')
    fptr.close()
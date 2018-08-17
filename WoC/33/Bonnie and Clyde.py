#!/bin/python3

import sys
from collections import deque
from itertools import chain


s2i=lambda i:int(i)-1
N, M, Q = map(int, input().strip().split())

P=[None]*N
R=list(range(N))
L=list(range(N))

def tr(G): # Transpose (rev. edges of) G
    GT=[[] for _ in range(N*2+2)]
    for u in range(len(G)):
        for v in G[u]:
            GT[v].append(u) # Add all reverse edges
    return GT

def paths(s, t, G, GT): # Edge-disjoint path count
    H, M, count = GT, set(), 0 # Transpose, matching, result
    while True: # Until the function returns
        Q, P = {s}, {} # Traversal queue + tree
        while Q: # Discovered, unvisited
            u = Q.pop() # Get one
            if u == t: # Augmenting path!
                count += 1 # That means one more path
                if count>1: return count
                break # End the traversal
            forw = (v for v in G[u] if (u,v) not in M) # Possible new edges
            back = (v for v in H[u] if (v,u) in M) # Cancellations
            for v in chain(forw, back): # Along out- and in-edges
                if v in P: continue # Already visited? Ignore
                P[v] = u # Traversal predecessor
                Q.add(v) # New node discovered
        else: # Didn't reach t?
            return count # We're done
        while u != s: # Augment: Backtrack to s
            u, v = P[u], u # Shift one step
            if v in G[u]: # Forward edge?
                M.add((u,v)) # New edge
            else: # Backward edge?
                M.remove((v,u)) # Cancellation

def merge(v1,v2):
    r1 = R[v1]
    r2 = R[v2]
    if r1 == r2:
        return
    r1, r2=min(r1,r2),max(r1,r2)
    P[r2]=L[r1]
    L[r1]=L[r2]
    v=L[r1]
    while R[v]==r2:
        R[v]=r1
        v=P[v]
        
def solve(u,v,w,G,GT):
    if u==v:
        res=paths(FOUT(u),FIN(w),G,GT)
    else:
        # xout -> u ... -> w
        #      -> v ... I
        xout=(N<<1)
        xin =(N<<1)+1
        G[xout]=[FIN(u),FIN(v)]
        res=paths(xout,FIN(w),G,GT)
        G[xout]=[]
    #print(res)
    return ("NO","YES")[res>=2]

FIN =lambda i:(i<<1)
FOUT=lambda i:(i<<1)+1

def task():        
    G =[[] for _ in range(N*2+2)]
    GT=[[] for _ in range(N*2+2)]
    #links
    for _ in range(M):
        x, y = map(s2i, input().strip().split())
        merge(x,y)
        #print(x,y)
        xin,xout=FIN(x),FOUT(x)
        yin,yout=FIN(y),FOUT(y)
        #print(xin,xout,yin,yout)
        #G
        if not G[xin]: G[xin].append(xout)
        if not G[yin]: G[yin].append(yout)
        G[xout].append(yin)
        G[yout].append(xin)
        #GT
        if not GT[xout]: GT[xout].append(xin)
        if not GT[yout]: GT[yout].append(yin)
        GT[xin].append(yout)
        GT[yin].append(xout)
    #print(G)          
    #print(GT)          
    #print(tr(G))
    for _ in range(Q):
        U, V, W = map(s2i, input().strip().split())
        if R[U]!=R[W] or R[V]!=R[W]:
            print("NO")
            continue
        print(solve(U,V,W,G,GT))

task()
#!/bin/python3

import sys


N,K,M = map(int, input().strip().split())
#parent
P=[None]*N
#root
R=list(range(N))
#last
L=list(range(N))

#main idea - each subgraph store as sequence of vertecis in order of finding to speed up traverse
#for each subgraph keep beginning and end of this sequence (root and last)
#for each vertice keep it's parent in sequence
#in such case joining of subgraphs means just corrrecting few values
#sure it can be done via list of sets of vertices... but slower %) Lets try
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

def lps(A):
    n = len(A)
 
    L = [[0]*n for _ in range(n)]
 
    for i in range(n):
        L[i][i] = 1
 
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if A[i] == A[j] and cl == 2:
                L[i][j] = 2
            elif A[i] == A[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j]);
    return L[0][n-1]    

for _ in range(K):
    x,y = map(int, input().strip().split())
    merge(x-1,y-1)

    

    
A = list(map(lambda x:R[int(x)-1], input().strip().split()))
#print(A)
print(lps(A))
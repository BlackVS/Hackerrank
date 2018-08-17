#!/bin/python3

import sys

DD = [ (-1,0), (1,0), (0,-1), (0,1) ]

def surfaceArea(A,H,W):
    # Complete this function
    res=0
    for r in range(H):
        for c in range(W):
            #top-bottom
            res+=2
            for dr,dc in DD:
                nr,nc=r+dr,c+dc
                if nr<0 or nc<0 or nr>=H or nc>=W:
                    res+=A[r][c]
                elif A[nr][nc]<A[r][c]:
                    res+=A[r][c]-A[nr][nc]
    return res
                
    
if __name__ == "__main__":
    H, W = map(int, input().strip().split(' '))
    A = []
    for _ in range(H):
        a = tuple(map(int, input().strip().split(' ')))
        A.append(a)
    result = surfaceArea(A,H,W)
    print(result)

import sys
from sys import stdin
input = stdin.readline

def solve(A,N,M):
    D=[[None]*M for _ in range(N)]
    #r=N-1
    DPFL=[0]*M
    DPFR=[0]*M
    for r in range(N):
        #maximum sums left/right for r,c (r.c not count)
        MSL=[0]*M
        for c in range(1,M):
            MSL[c]=max(0,MSL[c-1]+A[r][c-1])
        MSR=[0]*M
        for c in range(M-2,-1,-1):
            MSR[c]=max(0,MSR[c+1]+A[r][c+1])
        #print(A[r])
        #print(MSL,MSR)
        #now DP from left and from right separatly
        #DP From Left  = from left  + from top
        #DP From Right = from right + from top
        #really at r,c we should test from left, top, right. But we can't do it one pass - split in 2 ones
        #FROM LEFT
        if r==0:
            for c in range(M):
                D[r][c]=MSL[c]+A[r][c]+MSR[c]
            continue
        DPFL[0]=D[r-1][0]+A[r][0]
        for c in range(1,M):
            dt=D[r-1][c]+MSL[c]+A[r][c]
            dl=DPFL[c-1]+A[r][c]
            DPFL[c]=max(dt,dl)
        c=M-1
        DPFR[c]=D[r-1][c]+A[r][c]
        for c in range(M-2,-1,-1):
            dt=D[r-1][c]+MSR[c]+A[r][c]
            dr=DPFR[c+1]+A[r][c]
            DPFR[c]=max(dt,dr)
        #join
        for c in range(M):
            D[r][c]=max(DPFL[c]+MSR[c],DPFR[c]+MSL[c])
    return max(D[-1])

if __name__ == "__main__":
    N, M = map(int, input().strip().split(' '))
    if M==1:
        res=0
        for r in range(N):
            res+=int(input().strip())
        print(res)
    elif N==1:#classical Kadane
        max_ending_here = max_so_far = 0
        for a in map(int, input().strip().split(' ')):
            max_ending_here = max(0, max_ending_here + a)
            max_so_far = max(max_so_far, max_ending_here)
        print(max_so_far)    
    else:
        A = [[None]*M for _ in range(N)]
        for r in range(N):
            for c,a in enumerate(map(int, input().strip().split(' '))):
                A[r][c]=a

        print(solve(A,N,M))
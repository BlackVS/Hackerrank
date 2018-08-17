import sys

def getRect(r1,c1,r2,c2,XC):
    res=list(XC[r2][c2])
    if r1: 
        res[0]-=XC[r1-1][c2][0]
        res[1]^=XC[r1-1][c2][1]
    if c1: 
        res[0]-=XC[r2][c1-1][0]
        res[1]^=XC[r2][c1-1][1]
    if r1 and c1:
        res[0]+=XC[r1-1][c1-1][0]
        res[1]^=XC[r1-1][c1-1][1]

    return res

def CountBits(n):
    res=0
    while n:
        res+=n&1
        n>>=1
    return res

def isPalindrome(x1,y1,x2,y2,s):
    len=(x2-x1+1)*(y2-y1+1)
    #if len odd all must be even except one odd (center)
    #if len even all must even
    
    f=False
    if len&1:
        #odd 
        ss=CountBits(s[1])
        f= (ss==1) and (len==1 or s[0]<len-2)
    else:
        #even
        f= s[1]==0 and s[0]<len
    if f:
        return len
    return None

def solve(XC):
    #test from largest
    res_s=0
    res_r=(0,0,0,0)
    fstop=False
    #check edge
    if XC[N-1][M-1][0]==N*M:
        return (0,0,0,0)
   
    for rr in range(N,0,-1):
        if rr*M<=res_s: break
        Mmin=0
        if res_s: 
            Mmin=res_s//rr
        for cc in range(M,Mmin,-1):
            len=rr*cc
            if len<=res_s: break
            for r1 in range(0,N-rr+1):
                for c1 in range(0,M-cc+1):
                    r2=r1+rr-1
                    c2=c1+cc-1
                    if len>1 and XC[r2][c2][0]==len: continue
                    s=getRect(r1,c1,r2,c2,XC)
                    f=isPalindrome(r1,c1,r2,c2,s)
                    if f and f>res_s:
                        res_s=f
                        res_r=(r1,c1,r2,c2)
    return res_r

N, M = map(int, input().strip().split())
#map 0->1, 1->2, 2->4 etc
#prepare aux table for fast check 
XC=[ [ [0,0] for _ in range(M)] for _ in range(N)]
for r in range(N):
    for c,v in enumerate(map(int, input().strip().split())):
        vv=1<<v
        if r==0:
            XC[r][c][0]=(v==0)
            XC[r][c][1]=vv
        else:
            XC[r][c][0]=XC[r-1][c][0]+(v==0)
            XC[r][c][1]=XC[r-1][c][1]^vv
for r in range(N):
    for c in range(1,M):
        XC[r][c][0]+=XC[r][c-1][0]
        XC[r][c][1]^=XC[r][c-1][1]

res=solve(XC)
print( (res[2]-res[0]+1)*(res[3]-res[1]+1) )
print(res[0],res[1],res[2],res[3])

#!/bin/python3
import sys

NMOVES=( (-1,-2),(-1, 2),(-2,-1),(-2,1),(+1,-2),(+1, 2),(+2,-1),(+2,1) )

def isCheck(board, kr, kc, SQ, SR, SB, SN ):
    #QR
    # up
    c=kc
    for r in range(kr-1,-1,-1):
        if board[r][c]=='#': continue
        if board[r][c]==SQ or board[r][c]==SR:
            return True
        break
    # down
    c=kc
    for r in range(kr+1,8,1):
        if board[r][c]=='#': continue
        if board[r][c]==SQ or board[r][c]==SR:
            return True
        break
    # left
    r=kr
    for c in range(kc-1,-1,-1):
        if board[r][c]=='#': continue
        if board[r][c]==SQ or board[r][c]==SR:
            return True
        break
    # right
    r=kr
    for c in range(kc+1,8,1):
        if board[r][c]=='#': continue
        if board[r][c]==SQ or board[r][c]==SR:
            return True
        break
    #QB
    r,c=kr,kc
    while r>0 and c>0:
        r,c=r-1,c-1
        if board[r][c]=='#': continue
        if board[r][c]==SQ or board[r][c]==SB:
            return True
        break
    r,c=kr,kc
    while r>0 and c<7:
        r,c=r-1,c+1
        if board[r][c]=='#': continue
        if board[r][c]==SQ or board[r][c]==SB:
            return True
        break
    r,c=kr,kc
    while r<7 and c>0:
        r,c=r+1,c-1
        if board[r][c]=='#': continue
        if board[r][c]==SQ or board[r][c]==SB:
            return True
        break
    r,c=kr,kc
    while r<7 and c<7:
        r,c=r+1,c+1
        if board[r][c]=='#': continue
        if board[r][c]==SQ or board[r][c]==SB:
            return True
        break
    #N
    for dr,dc in NMOVES:
        r,c=kr+dr,kc+dc
        if r>=0 and c>=0 and r<8 and c<8 and board[r][c]=='N':
            return True
    return False


if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        board = [ ['#']*8 for _ in range(8) ]
        kr, kc = 0,0
        Kr, Kc = 0,0
        pawns=[]
        for r in range(8):
           s = input().strip()
           for c in range(8):
               v=s[c]
               board[r][c]=v
               if v=='k':
                   kr,kc=r,c
               if v=='K':
                   Kr,Kc=r,c
               if r==1 and v=="P":
                   pawns.append(c)

        res=0
        for pc in pawns:
            if board[0][pc]=='#':
                board[1][pc]='#'
                board[0][pc]='P'
                #check to check to whites
                if isCheck(board, Kr, Kc, 'q', 'r', 'b', 'n'):
                    board[1][pc]='P'
                    board[0][pc]='#'
                    continue

                for s in "QRBN":
                    board[0][pc]=s
                    res+=isCheck(board,kr,kc, 'Q', 'R', 'B', 'N')
                board[1][pc]='P'
                board[0][pc]='#'

        print(res)
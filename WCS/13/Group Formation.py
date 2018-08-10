#!/bin/python3
import sys
from collections import *

input = sys.stdin.readline

class Graph(object):
    def __init__(self,NS,GrpMin,GrpMax,G1MAX,G2MAX,G3MAX):
        #students
        self.NS=NS
        #min/max group size
        self.GrpMin=GrpMin
        self.GrpMax=GrpMax
        #max students for each grade
        self.GMAX=[G1MAX,G2MAX,G3MAX,GrpMax]
        #student name2idx, 0 based
        self.N2IDX  =defaultdict(lambda:None)
        self.IDX2N  =[None]*NS
        #
        self.NCurIdx=0
        self.SGRADE=[None]*NS
        #SubGraphs
        self.SB_P=None # cur group id
        self.SB_R=None # root
        self.SB_L=None # last
        self.SB_N=None # current number of groups
        #number of studenmts of each grade for each group
        self.SB_G=[[0,0,0,0] for _ in range(NS)]
        #current res
        self.RES_Gid=None
        self.RES_Gsz=0

    def addStudent(self,name,grade):
        idx=self.N2IDX[name]
        if idx==None:
            idx=self.NCurIdx
            self.N2IDX[name]=idx
            self.IDX2N[idx]=name
            self.NCurIdx+=1
            #each student is in own group at first and each id of group is eqult to id of root student
            self.SB_G[idx][grade]=1
            self.SB_G[idx][-1]=1

        self.SGRADE[idx]=grade
        return idx

    def merge(self,s1,s2):
        N=self.NS
        N2I=self.N2IDX
        I2N=self.IDX2N


        v1=N2I[s1]
        v2=N2I[s2]
        #init
        if not self.SB_P:
            self.SB_P=[None]*N
            self.SB_R=list(range(N))
            self.SB_L=list(range(N))
            self.SB_N=N
        P=self.SB_P #parent
        R=self.SB_R #root
        L=self.SB_L #end
        G=self.SB_G #count number of students of each grade in each group
        # get root of each
        r1 = R[v1]
        r2 = R[v2]
        if r1 == r2:
            #already in one subgraph
            return None
        #try join subgraphs
        #A) check total resulting group size
        #B) check each grade limits
        for i in range(4):
            if  G[r1][i]+G[r2][i]>self.GMAX[i]:
                return False
        # join
        r1, r2=min(r1,r2),max(r1,r2)
        P[r2]=L[r1] # link 2nd group to the end of first
        L[r1]=L[r2] # update L for first group
        L[r2]=None #just clean, not needed
        #update roots/group id for 2nd group
        v=L[r1]
        while R[v]==r2:
            R[v]=r1
            v=P[v]
        #update statistcis
        for i in range(4):
            G[r1][i]+=G[r2][i]
            G[r2][i]=0
        # current res
        if G[r1][-1]>self.RES_Gsz:
            self.RES_Gsz=G[r1][-1]
            self.RES_Gid=r1
        # count final groups
        self.SB_N-=1
        return True

    def printLargestGroup(self):
        N=self.NS
        GMIN=self.GrpMin
        N2I=self.N2IDX
        I2N=self.IDX2N
        R  =self.SB_R
        G  =self.SB_G

        if self.RES_Gsz<self.GrpMin:
            print("no groups")
            return
        #bisect!
        RES=[]
        for i in range(N):
            gid=R[i]
            if G[gid][-1]==self.RES_Gsz:
                RES.append(I2N[i])
        RES.sort()
        for r in RES:
            print(r)
        return


if __name__ == "__main__":
    N,Q,GrpMin,GrpMax,G1MAX,G2MAX,G3MAX = map(int, input().strip().split())
    G=Graph(N,GrpMin,GrpMax,G1MAX,G2MAX,G3MAX)
    for i in range(N,):
        name,grade=input().strip().split()
        G.addStudent(name,int(grade)-1)
    for q in range(Q):
        s1,s2=input().strip().split()
        G.merge(s1,s2)
    G.printLargestGroup()
#include <bits/stdc++.h>

#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <utility>
using namespace std;


#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))
#define boost std::ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)

typedef map<int, int> MII;

typedef long long ll;

typedef struct {
	int gsize; //size of group
	int gcount;//number of groups of size gsize
	ll  grest; //number of groups size greater or equal to gszie
} RA_REC;



class CTeams {
		int        m_NP;
		vector<int>    G_SZ;
		MII            G_SZcnt;
		vector<int>    SB_P;//prev
		vector<int>    SB_R;//root
		vector<int>    SB_L;//last
		vector<RA_REC> SB_RA;
        bool           RA_updated;
	public:
		CTeams(int N) : 
			m_NP(N),
			G_SZ(N,1)
			
		{
			G_SZcnt[1] = N;
			SB_P.resize(N, -1);
			SB_R.resize(N);
			SB_L.resize(N);
			for (int i = 0; i < N; i++) {
				SB_L[i] = SB_R[i] = i;
			}
			SB_RA.resize(N);
            RA_updated=false;
		}

		void join(int v1, int v2) {
			int r1 = SB_R[v1];
			int r2 = SB_R[v2];
			
			if (r1 == r2)
				return;

			if ( G_SZ[r1] < G_SZ[r2] )
				swap(r1, r2);

			SB_P[r2] = SB_L[r1];//link 2nd group to the end of first
			SB_L[r1] = SB_L[r2];//update L for first group
			SB_L[r2] = -1;		//just clean, not needed

			//update roots / group id for 2nd group
			int v = SB_L[r1];
			while (SB_R[v] == r2) {
				SB_R[v] = r1;
				v = SB_P[v];
			}
			//count final groups
			//self.NG -= 1
			int g1 = G_SZ[r1];
			G_SZcnt[g1]--; 
			if (G_SZcnt[g1] == 0) 
				G_SZcnt.erase(g1);
			int g2 = G_SZ[r2];
			G_SZcnt[g2] --;
			if (G_SZcnt[g2] == 0)
				G_SZcnt.erase(g2);
			//
			G_SZ[r1] += G_SZ[r2];
			G_SZ[r2] = 0;
			//
			G_SZcnt[G_SZ[r1]] ++;
			//check statistics, k - mumber of members,
			//s = sum(k*v for k, v in G_SR.items())
			//				assert(s == NP)
            RA_updated=false;
		}

		ll query(int c) {
			//c == 0
			if (c == 0) // #just count all non zero teams
			{
				ll res = 0;
				for (auto& g : G_SZcnt) {
					if (g.first > 0)
						res += g.second;
				}
				return res*(res - 1) / 2;
			}
			if (c >= m_NP)
				return 0;

			ll res = 0;
			//here is trick - map stores ordered by key value - needn't to sort
			
			MII& A = G_SZcnt;
			int N = (int)A.size();

			
			//update SB_RA with G_SZcnt, precalc
            if(!RA_updated){
                auto it = A.rbegin();
                SB_RA[N - 1].gsize  = it->first;
                SB_RA[N - 1].gcount = it->second;
                SB_RA[N - 1].grest  = it->second;
                it++;
                for (int i = N - 2; i >= 0; i--,it++) {
                    SB_RA[i].gsize = it->first;
                    SB_RA[i].gcount = it->second;
                    SB_RA[i].grest = SB_RA[i+1].grest + it->second;
                }
                RA_updated=true;
            }
			int j = 0;
			for (int i = 0; i < N; i++) {
				while (j < N && SB_RA[j].gsize < SB_RA[i].gsize + c)
					j++;
                if(j<N)
				    res += SB_RA[i].gcount * SB_RA[j].grest;
			}
			return res;
		}

};

int main() {
	int N, Q;
	boost;

	cin >> N >> Q;
	CTeams T(N);
	int c, a, b;
	for (int q = 0; q < Q; q++) {
		cin >> c;
		if (c == 1) {
			cin >> a >> b;
			T.join(a-1, b-1);
		}
		if (c == 2) {
			cin >> a;
			cout<<T.query(a)<<"\n";
		}
	}
}
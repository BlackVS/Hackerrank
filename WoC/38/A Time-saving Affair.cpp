#include <bits/stdc++.h>

#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <utility>
#include <queue>  
using namespace std;


#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))
#define boost std::ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)

typedef struct _EDGE {
	int node;
	int w;
	_EDGE(int _node, int _w) :
		node(_node),w(_w)
	{}
	bool operator<(const _EDGE &o) const
	{
		return w > o.w;
	}
} EDGE;


class Graph
{
	int VN;
	//int EN;
	std::vector<vector<EDGE>> adj;
public:
	Graph(int n);  // Constructor

	void addEdge(int v, int u, int w);
	int  getBestPath(int s, int t, int K);  
};

Graph::Graph(int n)
{
	VN = n;
	adj.resize(n);
}

void Graph::addEdge(int u, int v, int w)
{
	adj[u].push_back(EDGE(v,w));
	adj[v].push_back(EDGE(u,w));
}

int getWait(int t, int K) {
	div_t x = div(t, K);
	if ( (x.quot & 1) == 0)
		return 0;
	return K - x.rem;
}

int Graph::getBestPath(int s, int t, int K) {

	std::priority_queue< EDGE > Q;
	Q.push(EDGE(s,0));
	vector<bool> V(VN,false);
	while (!Q.empty()) {
		EDGE u = Q.top();
		Q.pop();
		int dd = getWait(u.w, K);
		if (!V[u.node]) {
			V[u.node] = true;
			if (u.node == t)
				return u.w;
			for (auto e : adj[u.node]) {
				if (!V[e.node])
					Q.push(EDGE(e.node, u.w + e.w + dd));
			}
		}
	}
	return -1;
}



int main() {
	int N, K, M;
	boost;

	cin >> N >> K >> M;
	Graph G(N);
	for (int q = 0; q < M; q++) {
		int u, v, w;
		cin >> u >> v >> w;
        if(u!=v)
		  G.addEdge(u-1, v-1, w);
	}
	int res = G.getBestPath(0, N - 1, K);
	//cout << res << endl;
    ofstream fout(getenv("OUTPUT_PATH"));
    fout << res << "\n";
    fout.close();
}
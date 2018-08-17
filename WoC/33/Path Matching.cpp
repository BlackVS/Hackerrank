#include <cstring>
#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;

int getshift(string str)
{
	if (str.length() == 0)
		return 0;
	char s = str[0];
	bool match = false;
	int end = 0;
	int i = 0;

	for (int k = 1; k < (int)str.length(); k++)
	{
		int c = str[k];
		if (!match) {
			if (c == s) {
				i = 1;
				match = true;
				end = k;
			}
		}
		else {
			if (c != str[i])
				match = false;
			i++;
		}
	}
	return match ? end : str.length();
}

class Graph
{
	int V;         
	std::vector<vector<int>> adj;
	int P[100001];
	string Labels;
	char PATH[100001];
public:
	Graph(int V,string& s);  // Constructor

	void addEdge(int v, int w); // function to add an edge to graph
	void BFS(int s,set<int> targets);  // prints BFS traversal from a given source s
	int  countSubs(const char* p, int shift = 1);
	string getPath(int v);
};

Graph::Graph(int N,string& s)
{
	V = N;
	adj.resize(N);
	Labels = s;
}

void Graph::addEdge(int v, int w)
{
	adj[v].push_back(w);
	adj[w].push_back(v);
}

void Graph::BFS(int root,set<int> targets) {
	memset(P, -1, V * 4);
	deque<int> queue; 
	queue.push_back(root);
	while (!queue.empty()&&!targets.empty()) {
		int u = queue.front();
		queue.pop_front();
		for (auto itv = adj[u].begin(); itv != adj[u].end(); itv++) {
			int v = *itv;
			if (P[v] != -1 || v == root)
				continue;
			P[v] = u;
			targets.erase(v);
			if (targets.empty())
				return;
			queue.push_back(v);
		}
	}
}

string Graph::getPath(int v) {
	int i = 0;
	PATH[i] = 0;
	while (v != -1) {
		PATH[i++]=Labels[v];
		v = P[v];
	}
	PATH[i] = 0;
	return PATH;
}

int  Graph::countSubs(const char* p,int shift) {
	int   count = 0;
	char* start = PATH;
	do {
		start = strstr(start, p);
		if (start) {
			count++;
			start+=shift;
		}
	} while (start);
	return count;
}
typedef struct
{
	int  v;
	bool f;
	int  i;
} DUV_item_t;

typedef std::vector<DUV_item_t> DUV_LIST;
typedef std::map<int, DUV_LIST > DUV_t;

int main() {
	int N, Q;
	string S;
	string p;
	cin >> N >> Q;
	cin >> S;
	cin >> p;
	string pi=p;
	std::reverse(pi.begin(), pi.end());
	int shiftP  = getshift(p);
	int shiftPI = getshift(pi);

	Graph G(N,S);
	for (int i = 0; i<N - 1; i++) {
		int u, v;
		cin >> u >> v;
		u--; v--;
		G.addEdge(u, v);
	}

	DUV_t  DUV;
	vector<int> res(Q, 0);
	vector<set<int>> GQ(N);
	for (int j = 0; j<Q; j++) {
		int u, v;
		bool f=false;
		cin >> u >> v;
		u--; v--;
		if (u > v) {
			swap(u, v);
			f = true;
		}
		GQ[u].insert(v);
		GQ[v].insert(u);
		DUV_item_t x = { v,f,j };
		DUV[u].push_back(x);
	}

	for (DUV_t::iterator it = DUV.begin(); it != DUV.end(); it++) {
		int u=it->first;
		G.BFS(u,GQ[u]);
		for (DUV_LIST::iterator itl = it->second.begin(); itl != it->second.end(); itl++) {
			DUV_item_t uv = *itl;
			//path is reversed!
			string path = G.getPath(uv.v);
			int cnt = 0;
			if (uv.f) {
				cnt = G.countSubs(p.c_str(), shiftP);
			}
			else {
				cnt = G.countSubs(pi.c_str(), shiftPI);
			}
			res[uv.i] = cnt;
		}
	}

	for (int i = 0; i < Q; i++)
		cout << res[i] << endl;
	return 0;
}

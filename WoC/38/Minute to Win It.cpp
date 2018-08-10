#include <bits/stdc++.h>


#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <unordered_map>


#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))
#define boost std::ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
using namespace std;
typedef long long LL;

int main() {
	LL  K, d = 0, a, c;
    int N, r = 0;
	boost;
	cin >> N >> K;
	unordered_map<LL, int> F;
	for (int i = 0; i < N; i++, d+=K) {
		cin >> a;
		a -= d;
		c = F[a] = F[a] + 1;
		r = MAX(c, r);
		//cout << a << " " << c << endl;
	}
    ofstream fout(getenv("OUTPUT_PATH"));
	//cout << N - r << endl;
    fout << N-r << "\n";
    fout.close();
}

#include <bits/stdc++.h>

#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
#include <utility>
using namespace std;


#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))
#define boost std::ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)

using namespace std;

typedef long long LL;

LL solve() {
	int N;
	cin >> N;

	std::vector<LL> H(N);
	//cin >> H[0];
	for (int i = 0; i < N; i++)
		cin >> H[i];

	std::vector<LL> W(N);
	W[0] = 0;
	for (int i = 1; i < N; i++)
		cin >> W[i];

	std::vector<LL> MC(N + 1, LLONG_MAX);
	MC[0] = 0;

	int i = 0;
	while(i<N) {
		int iNext = -1;
		for (int j = i + 1; j <= N; j++) {
			if (j == N) {
				if (MC[j] == LLONG_MAX)
					MC[j] = MC[i];
				else 
					MC[j] = MIN(MC[j], MC[i]);
				break;
			}
			if (W[j] <= 0 && iNext == -1)
				iNext = j;
			LL m = MC[i] + abs(H[j] - H[i]) + W[j];
			if (MC[j] == LLONG_MAX || m < MC[j])
				MC[j] = m;
			if (H[j] > H[i])
				break;
		}
		if (iNext == -1)
			i++;
		else
			i = iNext;
	}
	return MC[N] + N;
}

int main() {
	boost;

	cout << solve();
}
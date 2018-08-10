#include <bits/stdc++.h>

#include <stack>
#include <iostream>
#include <string>

using namespace std;

#define boost std::ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)

int solve(string s)
{
	stack<char> stack;
	for (int i = 0; i<s.length(); i++)
	{
		if (s[i] == ')' && !stack.empty())
		{
			if (stack.top() == '(' )
				stack.pop();
			else
				stack.push(s[i]);
		}
		else
			stack.push(s[i]);
	}

	char p = ' ';
	int cnt = 0;
	while(!stack.empty()) {
		char c = stack.top();
		if (c != p) {
			cnt++;
			p = c;
		}
		stack.pop();
	} 
	return cnt;
}

int main() {
	int n;
	string s;
	boost;
	cin >> n >> s;
	int res=solve(s);
    cout << res;
}

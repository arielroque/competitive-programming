#include <bits/stdc++.h>
using namespace std;

#define MAX 1000000

int n;
int arr[MAX];

bool dp(int i, int sum)
{
    if (i == n)
        return sum % 360 == 0;

    if (dp(i + 1, sum + arr[i]))
        return true;

    if (dp(i + 1, sum - arr[i]))
        return true;

    return false;
}

int main()
{
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    bool v = dp(1, arr[0]);

    if (v == 1)
    {
        cout << "YES";
    }

    else
    {
        cout << "NO";
    }

    return 0;
}
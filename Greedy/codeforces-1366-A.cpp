#include <bits/stdc++.h>

using namespace std;

int n;
long long x, y;

int getEmerald(long long x, long long y)
{

    long long z = (x + y) / 3;

    if (x < y && x < z)
    {
        return x;
    }
    else if (y < x && y < z)
    {
        return y;
    }

    else
    {
        return z;
    }
}

int main()
{

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> x >> y;
        long long r = getEmerald(x, y);
        cout << r << "\n";
    }

    return 0;
}
#include <bits/stdc++.h>
using namespace std;

int n;

int bills(int n, int size)
{
    if (n <= 0)
        return size;

    if (n % 100 == 0)
    {
        return bills(n - 100, size + 1);
    }

    if (n % 20 == 0)
    {
        return bills(n - 20, size + 1);
    }

    if (n % 10 == 0)
    {
        return bills(n - 10, size + 1);
    }

    if (n % 5 == 0)
    {
        return bills(n - 5, size + 1);
    }

    return bills(n - 1, size + 1);
}

int main()
{

    cin >> n;

    int r = bills(n, 0);

    cout << r;
}
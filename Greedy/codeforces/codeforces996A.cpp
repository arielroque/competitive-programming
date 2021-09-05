#include <bits/stdc++.h>

using namespace std;

long long getValue(long long n)
{
    long long qtd = 0;

    while (n > 0)
    {
        if (n % 100 == 0)
        {
            qtd++;
            n -= 100;
        }

        else if (n % 20 == 0)
        {

            qtd++;
            n -= 20;
        }

        else if (n % 10 == 0)
        {
            qtd++;
            n -= 10;
        }

        else if (n % 5 == 0)
        {

            qtd++;
            n -= 5;
        }

        else{
            qtd++;
            n -= 1;
        }
    }

    return qtd;
}

int main()
{

    long long n;

    cin >> n;

    int r = getValue(n);

    cout << r;

    return 0;
}
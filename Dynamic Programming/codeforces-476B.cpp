#include <bits/stdc++.h>

using namespace std;

string a, b;
int qtdC = 0;
int t = 0;

double dp(string value, int index, int total,int len, int sum, int unrecognized)
{
    if (index == len)

    {
        if (sum == total && unrecognized == 0)
        {
            return 1.000000000000;
        }
        else if (sum == total)
        {
            int p = pow(2, unrecognized);
            return (1.0 / p);
        }
        else{
            return 0;
        }
    }

    if (value[index] == '?')
    {
        return dp(value, index + 1, total,len, sum + 1, unrecognized + 1) + dp(value, index + 1, total,len, sum - 1, unrecognized + 1);
    }

    if (value[index] == '+')
    {
        return dp(value, index + 1, total,len, sum + 1, unrecognized);
    }
    else
    {
        return dp(value, index + 1, total,len, sum - 1, unrecognized);
    }
}

int main()
{

    cin >> a;
    cin >> b;

    int len = a.length();

    for (int i = 0; i < len; i++)
    {
        if (a[i] == '+')
        {
            t++;
        }
        else
        {
            t--;
        }
    }

    double r = dp(b, 0, t,len, 0, 0);

    cout << setprecision(9)<< r;

    return 0;
}
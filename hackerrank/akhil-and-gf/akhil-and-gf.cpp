#include<bits/stdc++.h>
#define long long long
using namespace std;

int power(unsigned long a, unsigned long b, unsigned long mod)  
{  
    int res = 1;  
    a = a % mod;
    if (a == 0) return 0;               // return 0 if a is divisble by mod
    while (b > 0)  
    {    
        if (b & 1)  res = (res*a) % mod;   // If b is odd, multiply a with result
        b = b >> 1;                       // Halving b
        a = (a*a) % mod;  
    }  
    return res;  
}

int main()
{
    int T;
    unsigned long N, M, no;
    cin >> T;
    while(T--)
    {
        cin >> N >> M;
        no = power(10, N, 9*M) - 1;        // Since 1111...N times = (10^N-1)/9
        cout << no/9 % M << endl;
    }
}
#include<bits/stdc++.h>
#define faster() ios_base::sync_with_stdio(false); cin.tie(NULL);
#define ll long long
using namespace std;

int main()
{
    faster()
    vector <ll> v={0};
    ll n, p;
    cin>>n;
    for(ll i=0; i<n; ++i)
    {
        cin>>p;
        if(p>v.back())
        {
            v.push_back(p);
        }
        else
        {
            *lower_bound(v.begin(), v.end(), p) = p;
        }           
    }
    cout<<n - v.size() + 1;
    return 0;
}
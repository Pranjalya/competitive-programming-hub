#include <ext/pb_ds/assoc_container.hpp> // Common file
#include <ext/pb_ds/tree_policy.hpp> // Including tree_order_statistics_node_update
#include <bits/stdc++.h>
#define ll long long
using namespace std;
using namespace __gnu_pbds;

typedef tree <int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

int main(int argc, char **argv)
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    ordered_set pos;
    int n, v;
    cin >> n;
    for(ll i=0; i<n; ++i)
    {
        cin >> v;
        pos.insert(v);
        cout << pos.size() - pos.order_of_key(v) << endl;
    }
    return 0;
}
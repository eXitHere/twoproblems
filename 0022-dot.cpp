#include<iostream>
using namespace std;

int main() {
    int n;
    int x,y;
    cin >> n;
    bool mark[1001][1001] = {0};
    int counter = 0;
    for(int i=0;i<n;i++) {
        cin >> x >> y;
        if(!mark[x][y]) {
            mark[x][y] = 1;
            counter += 1;
        }
    }
    cout << counter;
    return 0;
}
#include <bits/stdc++.h>

using namespace std;

int main() {
    int a = 1,b= 1,c= 1,d= 1, res;
    while(scanf("%d %d %d %d", &a, &b, &c, &d) && (a != 0 || b != 0 || c != 0 || d != 0)){
        res = 1080 + (((a-b+40)%40)+((c-b+40)%40)+((c-d+40)%40))*9;
        printf("%d\n", res);
    }
    return 0;
}
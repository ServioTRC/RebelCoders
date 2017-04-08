#include <bits/stdc++.h>

using namespace std;

int main() {
    int times, a, b;
    scanf("%d", &times);
    for(int i = 0; i < times; i++){
        scanf("%d %d", &a, &b);
        if(a < b){
            printf("<\n");
        } else if (a > b){
            printf(">\n");
        } else {
            printf("=\n");
        }
    }
    return 0;
}
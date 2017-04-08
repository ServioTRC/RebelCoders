#include <bits/stdc++.h>

using namespace std;

int main() {
    int times, rows, columns, temp;
    scanf("%d", &times);
    for(int i = 0; i < times; i++){
        scanf("%d %d", &rows, &columns);
        temp = columns / 3;
        temp *= rows / 3;
        printf("%d\n", temp);
    }
    return 0;
}
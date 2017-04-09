#include <bits/stdc++.h>

int main() {
    int cases, val;
    scanf("%d", &cases);
    for(int i = 0; i < cases; i++){
        scanf("%d", &val);
        val *= 567;
        val /= 9;
        val += 7492;
        val *= 235;
        val /= 47;
        val -= 498;
        val %= 100;
        val /= 10;
        if(val < 0)
            val *= -1;
        printf("%d\n", val);
    }
    return 0;
}
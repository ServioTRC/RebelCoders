#include <bits/stdc++.h>

using namespace std;

int main() {
    char caracter;
    bool executed = false, print;
    while(scanf("%c", &caracter)!=EOF){
        print = true;
        if(caracter == '"'){
            if(executed){
                printf("''");
                executed = false;
            }else{
                printf("``");
                executed = true;
            }
            print = false;
        }
        if(print)
            printf("%c", caracter);
    }
    return 0;
}
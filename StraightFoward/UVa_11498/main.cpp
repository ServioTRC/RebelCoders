#include <bits/stdc++.h>

using namespace std;

int main() {
    int queries, coordXCenter, coordYCenter, coordX, coordY;
    while(true){
        scanf("%d", &queries);
        if(queries == 0)
            break;
        scanf("%d %d", &coordXCenter, &coordYCenter);
        for(int i = 0; i < queries; i++){
            scanf("%d %d", &coordX, &coordY);
            if(coordX == coordXCenter || coordY == coordYCenter)
                printf("divisa\n");
            //Upper location
            else if(coordY > coordYCenter){
                if(coordX > coordXCenter)
                    printf("NE\n");
                else
                    printf("NO\n");
            }
            //Lower location
            else{
                if(coordX > coordXCenter)
                    printf("SE\n");
                else
                    printf("SO\n");
            }
        }
    }
    return 0;
}
#include <bits/stdc++.h>

using namespace std;

int main() {
    int count = 1;
    string pal;
    while(true){
        cin >> pal;
        if(pal == "*")
            break;
        else if(pal == "Hajj")
            cout << "Case " << count <<": Hajj-e-Akbar" << endl;
        else if(pal == "Umrah")
            cout << "Case " << count <<": Hajj-e-Asghar" << endl;
        count++;
    }
    return 0;
}
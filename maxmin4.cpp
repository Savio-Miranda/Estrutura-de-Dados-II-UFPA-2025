#include <iostream>
#include <utility>
using namespace std;

pair<int, int> maxmin4(int lim_inf, int lim_sup, int max, int min) {
    int max = vector[0];
    int min = vector[0];
    int lim_inf = vector[0];
    int lim_sup = vector[size];
    
    if(lim_sup - lim_inf <= 1){
        if(vector[lim_inf - 1] < vector[lim_sup - 1]){
            max = vector[lim_sup - 1];
            min = vector[lim_inf - 1];
        } else {
            max = vector[lim_inf - 1];
            min = vector[lim_sup - 1];
        }
    }
    int half = (lim_inf + lim_sup)/2;
    maxmin4(lim_inf, meio, max1, min1);
    maxmin4(meio + 1, lim_sup, max2, min2);
    if (max1 > max2){
        max = max1;
    } else {
        max = max2;
    }
    if (max1 < max2){
        min = min1;
    } else {
        min = min2;
    }

    return {max, min};
}

int main(){
    int vector[] = {3, 4, 2, 1, 6, 3, 12, 7, 5, 8};
    int size = sizeof(vector)/sizeof(vector[0]);
    pair<int, int> result = maxmin4(vector, size);
    cout << "Max: " << result.first << " Min: " << result.second << endl;
    return 0;
}
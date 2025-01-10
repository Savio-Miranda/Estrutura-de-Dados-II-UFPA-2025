#include <iostream>
#include <utility>
using namespace std;

pair<int, int> maxmin(const int vector[], int size) {
    int max = vector[0];
    int min = vector[0];

    for (int i = 1; i < size; i++) {
        if (vector[i] > max)
            max = vector[i];
        if (vector[i] < min)
            min = vector[i];
    }

    return {max, min};
}

int main(){
    int vector[] = {3, 4, 2, 1, 6, 3, 12, 7, 5, 8};
    int size = sizeof(vector)/sizeof(vector[0]);
    pair<int, int> result = maxmin(vector, size);
    cout << "Max: " << result.first << " Min: " << result.second << endl;
    return 0;
}
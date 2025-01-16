#include <iostream>
#include <utility>
using namespace std;

pair<int, int> maxmin2(const int vector[], int size) { // Custo total: O(n)
    int max = vector[0]; // c1: 1
    int min = vector[0]; // c2: 1

    for (int i = 1; i < size; i++) { // c3: n
        if (vector[i] > max){ // c4: n
            max = vector[i]; // c5: 1 <= t <= n
        }
        else if (vector[i] < min) { // c6: 1 <= t <= n
            min = vector[i]; // c7: 1 <= t <= n
        }
    }

    return {max, min}; // c8: 1
}

int main(){
    int vector[] = {3, 4, 2, 1, 6, 3, 12, 7, 5, 8};
    int size = sizeof(vector)/sizeof(vector[0]);
    pair<int, int> result = maxmin2(vector, size);
    cout << "Max: " << result.first << " Min: " << result.second << endl;
    return 0;
}
#include <vector>
#include <iostream>
using namespace std;

vector<int> maxmin4(const vector<int>& v, int linf, int lsup) {
    vector<int> maxMin(2); // c1: 1

    if ((lsup - linf) <= 1) { // c2: 0 ou 1
        if (v[linf] < v[lsup]) { // c3: 0 ou 1
            maxMin[0] = v[lsup]; // c4: 0 ou 1
            maxMin[1] = v[linf]; // c5: 0 ou 1
        } else { // c6: 0 ou 1
            maxMin[0] = v[linf]; // c7: 0 ou 1
            maxMin[1] = v[lsup]; // c8: 0 ou 1
        }
    } else { // c9: 0 ou 1
        int meio = (linf + lsup) / 2; // c10: 0 ou 1

        vector<int> maxMinLeft = maxmin4(v, linf, meio); // c11: T(n/2)
        vector<int> maxMinRight = maxmin4(v, meio + 1, lsup); // c12: T(n/2)

        // Combina os resultados
        maxMin[0] = max(maxMinLeft[0], maxMinRight[0]); // c13: 0 ou 1
        maxMin[1] = min(maxMinLeft[1], maxMinRight[1]); // c14: 0 ou 1
    }

    return maxMin; // c15: 1
}

int main() {
    // Exemplo de uso
    vector<int> v = {3, 1, 4, 12, 5, 9, 2, 0, 5};
    int linf = 0;
    int lsup = v.size() - 1;

    vector<int> result = maxmin4(v, linf, lsup);

    cout << "Máximo: " << result[0] << endl;
    cout << "Mínimo: " << result[1] << endl;

    return 0;
}
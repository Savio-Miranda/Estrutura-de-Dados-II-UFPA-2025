public class MaxMin4 {
    public static int[] maxMin4(int v[], int linf, int lsup) { // // Custo total: O(n*log(n))
        int maxMin[] = new int[2]; // c1: 1
        if ((lsup - linf) <= 1) { // c2: 1
            if (v[linf] < v[lsup]) { // c3: 0 ou 1
                maxMin[0] = v[lsup]; // c4: 0 ou 1
                maxMin[1] = v[linf]; // c5: 0 ou 1
            } else { // c6: 0 ou 1
                maxMin[0] = v[linf]; // c7: 0 ou 1
                maxMin[1] = v[lsup]; // c8: 0 ou 1
            }

        } else { // c9: 0 ou 1
            int meio = (linf + lsup) / 2; // c10: 0 ou 1
            maxMin = maxMin4(v, linf, meio); // c11: T(n/2)
            int max1 = maxMin[0]; // c12: 0 ou 1
            int min1 = maxMin[1]; // c13: 0 ou 1
            maxMin = maxMin4(v, meio + 1 , lsup); // c14: T(n/2)
            int max2 = maxMin[0]; // c15: 0 ou 1
            int min2 = maxMin[1]; // c16: 0 ou 1
            if (max1 > max2){ // c17: 0 ou 1
                maxMin[0] = max1; // c18: 0 ou 1
            } else { // c19: 0 ou 1
                maxMin[0] = max2; // c20: 0 ou 1
            }
            if (min1 < min2){ // c21: 0 ou 1
                maxMin[1] = min1; // c22: 0 ou 1
            } else { // c23: 0 ou 1
                maxMin[1] = min2; // c24: 0 ou 1
            }
        }
        return maxMin; // c25: 1
    }
}
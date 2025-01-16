def maxmin4(vector: list, linf: int, lsup: int):
    """
    Esta função tem custo 2T(n/2) + O(1), pois divide o vetor em dois
    a cada recursão. No entanto, resolvendo a recorrência temos que
    seu custo é linear.
    """
    maxmin = [0, 0]
    if (lsup - linf) <= 1:
        if vector[linf] < vector[lsup]:
            maxmin[0] = vector[lsup]
            maxmin[1] = vector[linf]
        else:
            maxmin[0] = vector[linf]
            maxmin[1] = vector[lsup]
    else:
        meio = (lsup + linf)//2
        maxmin = maxmin4(vector, linf, meio) # T(n/2)
        max1 = maxmin[0]
        min1 = maxmin[1]
        maxmin = maxmin4(vector, meio + 1, lsup) # T(n/2)
        max2 = maxmin[0]
        min2 = maxmin[1]

        if max1 > max2: 
            maxmin[0] = max1
        else:
            maxmin[0] = max2
        if min1 < min2:
            maxmin[1] = min1
        else:
            maxmin[1] = min2
    
    return maxmin

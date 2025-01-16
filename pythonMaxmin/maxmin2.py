def maxmin2(vector: list):
    """
    Esta função tem custo linear, mas com uma pequena melhor em relação à maxmin1,
    pois faz uma verificação a menos quando o primeiro if é satisfeito.
    """
    max = vector[0] # constante (1)
    min = vector[0] # constante (1)
    for i in range(1, len(vector)): # linear (1 até n)
        if vector[i] > max: # linear (1 até n)
            max = vector[i] # 0 ou até n vezes
        elif vector[i] < min: # 0 ou até n vezes
            min = vector[i] # 0 ou até n vezes
    
    return max, min # constante (1)
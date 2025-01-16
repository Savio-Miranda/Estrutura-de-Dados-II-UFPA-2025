
def maxmin(vector: list):
    """
    Esta função tem custo linear.
    """
    max = vector[0] # constante (1)
    min = vector[0] # constante (1)
    for i in range(1, len(vector)): # linear (1 até n)
        if vector[i] > max: # linear (1 até n)
            max = vector[i] # 0 ou até n vezes
        if vector[i] < min: # linear (1 até n)
            min = vector[i] # 0 ou até n vezes
    
    return max, min # constante (1)


def maxmin3(vector: list):
    """
    Implementação do algoritmo MaxMin3.
    Divide os elementos da lista em pares, comparando os elementos entre si
    e atualizando os valores de máximo e mínimo de forma otimizada.
    """
    # Caso a lista tenha apenas um elemento
    if len(vector) == 1:
        return vector[0], vector[0]

    # Inicializando os valores de máximo e mínimo
    if len(vector) % 2 == 0:  # Se o tamanho for par
        max_val = max(vector[0], vector[1])
        min_val = min(vector[0], vector[1])
        start = 2
    else:  # Se o tamanho for ímpar
        max_val = min_val = vector[0]
        start = 1

    # Percorrendo a lista em pares
    for i in range(start, len(vector), 2):
        if vector[i] > vector[i + 1]:
            max_val = max(max_val, vector[i])
            min_val = min(min_val, vector[i + 1])
        else:
            max_val = max(max_val, vector[i + 1])
            min_val = min(min_val, vector[i])

    return max_val, min_val


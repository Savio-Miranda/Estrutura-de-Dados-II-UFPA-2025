import time
import random
import matplotlib
import matplotlib.pyplot as plt

from maxmin1 import maxmin as mm1
from maxmin2 import maxmin2 as mm2
from maxmin3 import maxmin3 as mm3
from maxmin4 import maxmin4 as mm4

"""
No teste empírico fica claro que a função de maior custo computacional é
a maxmin4, pois é uma função n*log(n), portanto, quanto maior a entrada
mais instruções são executadas.
"""

pontos = {"maxmin1": [], "maxmin2": [], "maxmin3" : [], "maxmin4": []}

for exp in range(5):
    vector = []
    for exp in range(10**(exp + 1)):
        vector.append(random.randint(0, 100000))

    start_time = time.time()
    mm1(vector)
    pontos["maxmin1"].append(time.time() - start_time)
    
    start_time = time.time()
    mm2(vector)
    pontos["maxmin2"].append(time.time() - start_time)

    start_time = time.time()
    mm3(vector)
    pontos["maxmin3"].append(time.time() - start_time)

    start_time = time.time()
    mm4(vector, 0, len(vector) - 1)
    pontos["maxmin4"].append(time.time() - start_time)

x = [10**(exp + 1) for exp in range(5)] # entradas
# Criar o gráfico
plt.figure(figsize=(8, 6))

# Plotar cada função
plt.plot(x, pontos["maxmin1"], label='maxmin1', color='blue', linestyle='-')
plt.plot(x, pontos["maxmin2"], label='maxmin2', color='red', linestyle='--')
plt.plot(x, pontos["maxmin3"], label='maxmin3', color='black', linestyle=':')
plt.plot(x, pontos["maxmin4"], label='maxmin4', color='green', linestyle='-.')

# Configurações do gráfico
plt.title("Maxmin para entradas cada vez maiores")
plt.xlabel("Entradas (tamanho do vetor)")
plt.ylabel("Tempo")
plt.legend()  # Mostrar a legenda
plt.grid(True)  # Adicionar uma grade
plt.tight_layout()  # Ajustar margens

# Exibir o gráfico
plt.show()

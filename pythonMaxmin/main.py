import time
import random

from maxmin1 import maxmin as mm1
from maxmin2 import maxmin2 as mm2
from maxmin4 import maxmin4 as mm4

# CONSTRUINDO VETOR
vector = []
for i in range(999999):
    vector.append(random.randint(0, 1000000))

# vector = [4, 5, 32, 6, 3, 2, 7, 9, 23] # teste em vetor menor

# TESTE EMPÍRICO
start_time = time.time()
print(f"maxmin (versão 1): {mm1(vector)}")
print("-> %s segundos" % (time.time() - start_time))

start_time = time.time()
print(f"maxmin (versão 2): {mm2(vector)}")
print("-> %s segundos" % (time.time() - start_time))

start_time = time.time()
print(f"maxmin (versão 4): {mm4(vector, 0, len(vector) - 1)}")
print("-> %s segundos" % (time.time() - start_time))

"""
No teste empírico fica claro que a função de maior custo computacional é
a maxmin4, pois embora ela seja linear, possui mais instruções a serem
executadas. Ainda por cima é recursiva, que em tarefas CPU-Bound como
essas podem estourar a memória.
"""
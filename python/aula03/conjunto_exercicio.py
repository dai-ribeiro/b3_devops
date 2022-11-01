# Exercício:

# 1. Gere um conjunto com 20 números aleatórios entre 1 e 25
import random

aleatorio = set()
while len(aleatorio) <20:
    aleatorio.add(random.randint(1, 25))

print(aleatorio)

# 2. Gere um segundo conjunto com 20 números aleatórios entre 5 e 30
numeros = set()

while len(numeros) < 20:
    numeros.add(random.randint(5, 30))

print(numeros)

# 3. Calcule:
#     3.1. se são conjuntos disjuntos
print(aleatorio.isdisjoint(numeros))

#     3.2. a interseção
print(aleatorio.intersection(numeros))

#     3.3. a união
print(aleatorio.union(numeros))

#     3.4. a diferença simétrica
print(aleatorio.symmetric_difference(numeros))

#
# Para geração dos números aleatórios, utilize a função nativa do python:
#
#     import random
#     random.randint(inicio, fim)




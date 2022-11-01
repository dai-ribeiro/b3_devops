"""
### Conjunto (set) ###

definição: é um container que armazena itens não ordenados/sequenciados, mutáveis e iteráveis
mas sem elementos duplicados.
"""

# criando um conjunto
conj = {1, 2, 3, 4, 5}


# verificando o tipo
type(conj)


# criando um conjunto misto
mista = {1, 2, 3.1415, 'a', 'isto é uma frase', (1, 2, 3)}


# acessando elementos do conjunto (slice / slicing)
## diferente de listas e tuplas, conjuntos são objetos não sequenciais, ou seja, não tem uma posição
## definida, o que impossibilita realizar o slice.
# conj[0]   -> ocorre TypeError, não conseguimos acessar posições


## realizando a instrospecção do objeto set, observamos que não possui o método __getitem__, logo não temos acesso
## ao slice do objeto
dir(conj)


# conjuntos são mutáveis
## podemos adicionar e remover elementos

## método add
conj.add(6)


## método remove
conj.remove(6)


# conjuntos são iteráveis (__iter__)
for i in conj:
    print(i)


# conjuntos remove duplicados
lista = (1, 2, 3, 2, 3, 6, 7, 8, 1, 10)
set(lista)


# Operações de conjunto
A = {1, 2, 3, 4, 5}
B = {1, 3, 5, 7, 9}


## interseção
A.intersection(B)

## união
A.union(B)

## diferença
A - B
B - A

## diferença simétrica
A.symmetric_difference(B)


## disjunção
A.isdisjoint(B)


"""
Exercício:

1. Gere um conjunto com 20 números aleatórios entre 1 e 25
2. Gere um segundo conjunto com 20 números aleatórios entre 5 e 30
3. Calcule:
    3.1. se são conjuntos disjuntos
    3.2. a interseção
    3.3. a união
    3.4. a diferença simétrica
    
Para geração dos números aleatórios, utilize a função nativa do python:

    import random
    random.randint(inicio, fim)

"""

import random

# 1. Gere um conjunto com 20 números aleatórios entre 1 e 25
# 2. Gere um segundo conjunto com 20 números aleatórios entre 5 e 30

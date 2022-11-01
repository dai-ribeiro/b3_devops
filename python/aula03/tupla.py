"""
### Lista (list) ###

definição: é um container que armazena elementos/objetos
de forma sequencial, mutável e iterável.

### Tupla (tuple) ###

definição: é um container que armazena elementos/objetos
de forma sequencial, imutável e iterável.
"""

# criando uma tupla
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)


# verificando o tipo
type(tupla)


# criando uma tupla mista
mista = (1, 2, 3.1415, 'a', 'isto é uma frase', [1, 2, 3])


# acessando elementos da tupla (slice / slicing)
## assim como listas, tuplas armazenam sequencias de objetos que podem ser acessados por suas posições
tupla[0]        # pega o primeiro elemento
tupla[-1]       # pega o último elemento
tupla[4]        # pega o último elemento
tupla[1:3]      # pegao o primeiro e segundo elemento
tupla[::2]      # pega todos os elementos de dois em dois
tupla[::-1]     # inverte a ordem dos elementos


# tuplas são imutáveis
## isso significa que uma vez criadas, não podemos alterar, adicionar ou remover elementos da mesma
# tupla[0] = 10 -> RETORNA UM ERRO


# desempacotamento de tupla
nome, sobrenome, idade = ('leonardo', 'borges', 34)


# tuplas são iteráveis
## por possuir os métodos __iter__ e __getitem__, tuplas podem ser iteradas
tuplas = (('bruna', 'luchini'), ('fulana', 'de tal'))
for (nome, sobrenome) in tuplas:
    print(nome, sobrenome)


# convertendo listas para tuplas
tuple(lista)


# convertendo tuplas para listas
list(tupla)


"""
Exercício:

1. Crie uma lista de compras com 5 elementos
2. Transforme a lista em tupla
3. Imprima os 3 elementos centrais utilizando slice
4. Itere sobre os itens da tupla e imprima: o nome do item e quantas letras ele possui
"""

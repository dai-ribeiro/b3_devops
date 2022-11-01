# Exercício:

# 1. Crie uma lista de compras com 5 elementos
lista = ['pera', 'uva', 'maça', 'banana', 'morango']

# 2. Transforme a lista em tupla
tupla = tuple(lista)

# 3. Imprima os 3 elementos centrais utilizando slice
print(tupla[1:4])
print()

# 4. Itere sobre os itens da tupla e imprima: o nome do item e quantas letras ele possui
for item in tupla:
    print(item, len(item))
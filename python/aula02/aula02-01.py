'''
Lista de compras

Crie um programa que leia a quantidade de itens que precisamos comprar no mercado.
Logo após, o programa deve perguntar o nome de todos os itens e colocar em uma lista de compras.
Por último, o programa deve imprimir todos os itens da lista.
'''

qtd = int(input('Quantos itens deseja comprar? '))
lista = []

for i in range(qtd):
    produto = input('Digite o produto: ')
    lista.append(produto)

print(lista)

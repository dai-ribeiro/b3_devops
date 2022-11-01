"""
Exercício:

1. Criar uma função de cadastro de contatos na agenda (dicionário)
2. Dicionário com uma lista de contatos contendo: nome, telefone e email
3. Cadastrar 3 contatos na agenda utilizado a função

Bônus:
    1. Criar função que busca a retorna um contato a partir do nome
    2. Criar função de deleta um contato a partir do nome
    3. Criar função de atualiza os dados de contato a partir do nome
"""

import crud
from pprint import pprint

agenda = {
    'contatos': []
}

novo_contato1 = {
    'nome': 'leo',
    'tel:': '11 12345678',
    'email': 'leo@leo.com'
}

novo_contato2 = {
    'nome': 'matheus',
    'tel:': '11 234567890',
    'email': 'matheus@mat.com'
}

novo_contato3 = {
    'nome': 'ada',
    'tel:': '11 12341234',
    'email': 'ada@lovelace.com'
}

crud.criar_contato(agenda, novo_contato1)
crud.criar_contato(agenda, novo_contato2)
crud.criar_contato(agenda, novo_contato3)

print('1. Criar contato:')
pprint(agenda)


print('\n2. Buscar contato:')
buscar_nome = 'bete'
contato = crud.buscar_contato(agenda, buscar_nome)
pprint(contato)


# TODO: não está removendo
print('\n3. Remover contato:')
remover_nome = 'matheus'
agenda = crud.remover_contato(agenda, remover_nome)
pprint(agenda)


# TODO: não ta localizando os nomes
print('\n4. Atualizar contato:')
atualizar_nome = 'leo'
atualizar_dados = {
    'tel': '22 98765432',
    'email': 'mat@mat.com'
}
agenda = crud.atualizar_contato(agenda, atualizar_nome, atualizar_dados)
pprint(agenda)
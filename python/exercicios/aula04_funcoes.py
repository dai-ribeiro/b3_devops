# Aula 04 - Funções
# 1. Criar uma função de cadastro de contatos na agenda (dicionário)
# 2. Dicionário com uma lista de contatos contendo: nome, telefone e email
# 3. Cadastrar 3 contatos na agenda utilizado a função

import crud

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

print(agenda)


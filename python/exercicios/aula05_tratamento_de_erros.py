'''
Aula 05 - Tratamento de Erros

1. Use o seu código produzido para o exercício da aula 04, para aplicar os
devidos tratamentos de erros usando o Try e Except da forma que julgar
necessário.
'''
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
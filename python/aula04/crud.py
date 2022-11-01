'''
Descricao
Autor: Daiane
'''

def buscar_contato(agenda, nome):
    for indice, contato in enumerate(agenda['contatos']):
        if nome == agenda['contatos']:
            return indice, contato
    return None, None


def criar_contato(agenda, dados_contato):
    # buscar contato
    # se ele existir:
    #     nao cria
    #     escreve uma mensagem de contato existente
    # caso contrario:
    #     cria contato
    agenda['contatos'].append(dados_contato)
    return agenda


def remover_contato(agenda, nome):
    indice, contato = buscar_contato(agenda, nome)
    if contato:
        agenda['contatos'].pop(indice)
        return agenda
    else:
        print('contato não existe')
        return agenda

def atualizar_contato(agenda, nome, dados_contato):
    indice, contato = buscar_contato(agenda, nome)
    for key, value in dados_contato.items():
        agenda['contatos'][indice][key] = value
    return agenda
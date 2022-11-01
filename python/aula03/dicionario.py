"""
### Dicionário (dict) ###

definição: é um container que armazena elementos/objetos  de forma
não sequencial, mutável e iterável, permitindo valores repetidos, mas não chaves
"""

# criando um dicionário
dicio = {'a': 1, 'b': 2, 'c': 3}


# verificando o tipo
type(dicio)


# criando um dicionario complexo
complex = {
    'inteiro': 8,
    'float': 3.1415,
    'string': 'um texto qualquer',
    'lista': [1, 2, 3],
    'tupla': (1, 6, 22),
    'dicio': {
        'rua': 'nome da rua',
        'numero': 240
    }
}


# acessando os elemento da tupla
## diferente de listas e tuplas, o acesso não é posicional, mas pela chave
dicio['a']
complex['lista'][1]
complex['dicio']['numero']


# dicionários são mutáveis
## podemos adicionar e remover elementos, podemos também valores mas não as chaves
complex['dicio']['numero'] = 360    # atualiza o valor
complex['lista'].append(4)
complex['dicio']['bairro'] = 'jardins'
complex.pop('inteiro')


# dicionários são iteráveis
for i in complex:
    print(i)    # retorna apenas a chave

for key in complex:
    print(key, complex[key])    # retorna chave e valor

for chave, valor in complex.items():
    print(chave, valor)     # retorna chave e valor


# métodos de dicionário
## novo dicionário de compras contendo item e quantidade
compras = {
    'arroz': 1,
    'feijao': 3,
    'chocolate': 1,
    'requeijao': 2
}


## método keys
compras.keys()


## método values
compras.values()


## verificando de tem um item no dicionario
'abobrinha' in compras.keys()
'chocolate' in compras.keys()


"""
Exercício:

1. Crie uma agenda utilizando dicionário, a agenda deve ter uma lista de 3 contatos.
2. Os contatos, além do nome, devem possuir telefone e email
3. Verifique se há algum contato com o nome 'marcos'
4. altere o telefone do primeiro contato
5. calcule quanto contatos possuem na lista
"""

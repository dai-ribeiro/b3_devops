"""
### Função (function) ###

definição: sequencia nomeada de instruções que encapsula um trecho
de código, podendo ser chamada sempre que necessária pelo seu nome.

aplicações:
- dry (don't repeat yourself)
- apoia automação
- apoia na organização e separação lógica
- apoia na manutenção do código

"""

# definindo uma função

# def nome_da_funcao(parametros):
#     // bloco de código
#     return valor(es)


# função sem argumentos e sem retorno
def print_ola_mundo():
    print('Olá mundo!')


# função com argumentos e sem retorno
def print_ola(nome):
    print(f'Olá, {nome}!')


# função com argumentos posicionais e um retorno
def soma(a, b):
    '''
        soma a e b com paramentros posicionais.
        esses parametros sao obrigatorios.
    '''
    return a + b


# função com argumentos posicionais e um multiplos retornos
def soma_mult(a, b):
    resultado = a + b
    return a, b, resultado


# função com argumentos nomeados e com retorno
def soma_nom(a=10, b=20):
    '''
        soma a e b com argumentos nomeados.
        sao argumentos opcionais.

    :param a: descricao do parametro. Default é 10.
    :param b: descricao do parametro. Default é 20.
    :return:
    '''
    print(f'a={a} e b={b}')
    return a + b


# função com argumentos posicionais, nomeados e com retorno
def soma_misto(a, b, c=0, d=0):
    print(f'a={a} | b={b} | c={c} | c={c}')
    res1 = a + b
    res2 = c + d
    return res1, res2

def func(n1, n2):
    return n1 + n2, n1 * n2

# ERRO PQ O POSICIONAL DEVE VIR PRIMEIRO
# def func_erro(a=0, b):
#     return a + b

def func_erro_com_nolfix(b, a=10):
    return a + b

# dicionário como argumentos nomeados
media_params = {
    'a': 2, 'b': 10, 'c': 2, 'd': 20, 'e': 100
}

def media_simples(a, b, c, d=0, e=0):
    res = (a + b + c + d + e) / 5
    return res

# media_simples(10, **params)
# media_simples(*params.values())


# criando uma função que calcula média a partir de uma lista
# inputs = lista com inteiros ou floats

def media_lista(lista):
    media = sum(lista) / len(lista)
    return media



# criando uma função que calcula a área de um retangulo

def calcula_area(base, altura):
    area = (base * altura) / 2
    return area


# criando uma função que calcula a área de um triangulo
import math

def area_triang(base, altura):
    return (base * altura)


# criando um modulo para funções geometricas
import geometria
print(geometria.area_triang(2,4))

from geometria import area_circ
print(area_circ(5))




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


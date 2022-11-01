cadastro = ['Adriele, 25, Desenvolvedor Web', 'Gabriela, 35, Desenvolvedor BackEnd',\
            'Leonardo, 29, DataScience', 'Carlos, 33, dev']

def dados_processados(cadastros):
    for cadastro in cadastros:
        dados = cadastro.split(',')

    if len(dados) != 3:
        raise ValueError('Formato incorreto de dados no cadastro.')

        nome = dados[0]
        idade = int(dados[1])
        cargo = dados[2]

    print(f"{nome} tem {idade} e exerce o papel de {cargo}")

try:
    dados_processados(cadastro)

except ValueError as exc:
    print(f'O programa detectou o seguinte erro: {exc}')


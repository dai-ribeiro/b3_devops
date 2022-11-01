###### BIBLIOTECAS ######
from datetime import date


###### FUNCOES ######

def atualizar_usuario(nome_arquivo, cadastro, usuario, dados_atualizados, nome_original):
    usuario_atualizado = []
    if usuario:
        print(usuario)
        for pos, dado in enumerate(usuario):
            novo_dado = dados_atualizados[pos]
            usuario_atualizado.append(novo_dado)
        cadastro.append(usuario_atualizado)

        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_escrita:
            for usuario in cadastro:
                for dado in usuario:
                    arquivo_escrita.write(f'{dado},')
                arquivo_escrita.write('\n')
        # TODO: REMOVER A MSG DE REMOCAO DO USUARIO
        cadastro = remover_usuario(nome_arquivo, nome_original)


def buscar_usuario(nome_arquivo, nome):
    cadastro = ler_arquivo(nome_arquivo)
    for id, usuario in enumerate(cadastro):
        if usuario[0] == nome:
            return cadastro, id, usuario
    return None, None, None


def cadastrar_usuario(nome_arquivo, nome, genero, email, telefone, cpf, data_nascimento):
    idade = calcular_idade(data_nascimento)
    usuario = {
        'nome': nome,
        'genero': genero,
        'email': email,
        'telefone': telefone,
        'cpf': cpf,
        'data de nascimento': data_nascimento,
        'idade': idade
    }
    gravar_arquivo(nome_arquivo, usuario)
    print(f'Cadastro do usuário {nome} realizado com sucesso!')


def calcular_idade(data_nascimento):
    data_nascimento_processada = data_nascimento.split('/')
    data_nascimento_processada = date(int(data_nascimento_processada[2]), int(data_nascimento_processada[1]), int(data_nascimento_processada[0]))
    data_hoje = date.today()
    idade = data_hoje.year - data_nascimento_processada.year - ((data_hoje.month, data_hoje.day) < (data_nascimento_processada.month, data_nascimento_processada.day))
    return idade


def criar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        titulo = ['NOME', 'GÊNERO', 'E-MAIL', 'TELEFONE', 'CPF',  'DATA DE NASCIMENTO', 'IDADE']
        for item in titulo:
            arquivo.write(f'{item},')
        # arquivo.write('IDADE')
        arquivo.write('\n')


def estatisticas(nome_arquivo):
    cont, cont_f, cont_18, cont_35, cont_65, cont_100 = -1, 0, 0, 0, 0, 0

    with open('./cadastro_usuarios.txt', 'r') as arquivo:
        lista = arquivo.readlines()
        for i in lista:
            try:
                cont += 1
                lista_item = i.split(',')
                if lista_item[1] == 'F':
                    cont_f += 1
                if int(lista_item[-2]) < 18:
                    cont_18 += 1
                elif int(lista_item[-2]) < 35:
                    cont_35 += 1
                elif int(lista_item[-2]) < 65:
                    cont_65 += 1
                else:
                    cont_100 += 1
            except:
                pass

    print(f'''
    A quantidade de usuários cadastrados é {cont}.
    A quantidade de usuários cadastrados do gênero feminino é {cont_f}.
    A quantidade de usuários cadastrados do gênero masculino é {cont - cont_f}.
    A quantidade de usuários cadastrados menores de 18 anos é {cont_18}.
    A quantidade de usuários cadastrados com idade entre 18 e 35 anos é {cont_35}.
    A quantidade de usuários cadastrados com idade entre 35 e 65 anos é {cont_65}.
    A quantidade de usuários cadastrados maiores de 65 anos é {cont_100}''')


def gravar_arquivo(nome_arquivo, usuario):
    with open(nome_arquivo, 'a', encoding='utf-8') as arquivo_escrita:
        for k, v in usuario.items():
            arquivo_escrita.write(f'{str(v)},')
        arquivo_escrita.write('\n')


def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_leitura:
        cadastro = []
        for linha in arquivo_leitura.readlines():
            dado = linha.split(',')
            cadastro.append(dado[:-1])  # estava pegando no final uma quebra de linha '\n' como elemento da lista
        return cadastro


def ler_opcao(msg, lista_range):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError) as erro:
            print(f'Opção inválida! Erro detectado: {erro}.')
        else:
            if num in lista_range:
                return num
                break
            print(f'Opção inválida! Responda um número entre {lista_range[0]} e {lista_range[-1]}.')


def linha(simbolo='-', tamanho=50):
    print(simbolo * tamanho)


def menu(lista, simbolo='-', tamanho=50):
    titulo('MENU', simbolo, tamanho)
    cont = 1
    for item in lista:
        print(f'[{cont}] {item}')
        cont += 1
    linha(simbolo, tamanho)
    opcao = ler_opcao('Informe sua opção: ', range(1, cont))
    return opcao


def remover_usuario(nome_arquivo, nome):
    cadastro, id, usuario = buscar_usuario(nome_arquivo, nome)
    if usuario:
        cadastro.pop(id)
        print(f'Remoção do usuário {nome} do cadastro realizada com sucesso!')

    else:
        print(f'Não há nenhum usuário no cadastro com o nome {nome}.')

    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_escrita:
        for usuario in cadastro:
            for dado in usuario:
                arquivo_escrita.write(f'{dado},')
            arquivo_escrita.write('\n')
    return cadastro


def titulo(texto, simbolo='=', tamanho=50):
    linha(simbolo, tamanho)
    print(f'{texto:^{tamanho}}')
    linha(simbolo, tamanho)


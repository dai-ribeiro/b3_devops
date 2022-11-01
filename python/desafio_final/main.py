from funcoes import *
from os.path import isfile
from time import sleep

arquivo_cadastro = 'cadastro_usuarios.txt'

titulo('INÍCIO DO PROGRAMA')

if isfile(arquivo_cadastro) is False:
    criar_arquivo(arquivo_cadastro)

while True:
    opcao = menu(['Exibir lista de usuários', 'Buscar usuário', 'Cadastrar usuário', 'Remover usuário',\
                       'Atualizar dados do usuário', 'Estatísticas do sistema', 'Sair'], simbolo='-', tamanho=50)


    if opcao == 1:
        linha('-', 140)
        cadastro = ler_arquivo('cadastro_usuarios.txt')
        for usuario in cadastro:
            for dado in usuario:
                if dado == usuario[-1]:
                    dado = dado.replace('\n', '')
                print(f'{dado:^20}', end='')
            print()
        linha('-', 140)

    elif opcao == 2:
        nome = input('Insira o nome do usuário que deseja buscar no cadastro: ').capitalize().strip()
        cadastro, id, usuario = buscar_usuario(arquivo_cadastro, nome)
        if usuario:
            for dado in usuario:
                print(f'{dado:^20}', end='')
            print()
        else:
            print(f'Não foi encontrado o usuário: {nome}.')

    elif opcao == 3:
        nome = input('Nome: ').strip().capitalize()
        # TODO: validar genero
        genero = input('Gênero [M/F]: ').strip().upper()
        # TODO: validar email
        email = input('E-mail: ').strip().lower()
        # TODO: validar telefone
        telefone = input('DDD + Telefone: ').strip()
        # TODO: validar cpf
        cpf = input('CPF [XXX.XXX.XXX-XX]').strip()
        # TODO: validar nascimento
        data_nascimento = input('Data de Nascimento [dd/mm/aaaa]: ').strip()
        cadastro = cadastrar_usuario(arquivo_cadastro, nome, genero, email, telefone, cpf, data_nascimento)

    elif opcao == 4:
        nome = input('Insira o nome do usuário que deseja remover: ').capitalize().strip()
        remover_usuario(arquivo_cadastro, nome)

    # TODO: dando erro (verificar)
    elif opcao == 5:
        nome_original = input('Insira o nome o usuário que deseja atualizar: ').capitalize().strip()
        if usuario:
            nome = input('Nome: ').strip().capitalize()
            genero = input('Gênero [M/F]: ').strip().upper()
            email = input('E-mail: ').strip().lower()
            telefone = input('DDD + Telefone: ').strip()
            cpf = input('CPF [XXX.XXX.XXX-XX]: ').strip()
            data_nascimento = input('Data de nascimento [dd/mm/aaaa]: ').strip()
            idade = calcular_idade(data_nascimento)
            dados_atualizados = [nome, genero, email, telefone, cpf, data_nascimento, idade]
            cadastro = atualizar_usuario(arquivo_cadastro, cadastro, usuario, dados_atualizados, nome_original)
        else:
            print(f'Não há usuário com o nome: {nome_original}')

    elif opcao == 6:
        estatisticas(arquivo_cadastro)

    else:
        break
    sleep(3)

titulo('PROGRAMA FINALIZADO')


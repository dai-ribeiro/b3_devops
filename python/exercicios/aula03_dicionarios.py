# Aula 03 - Dicionários
# 1. Crie uma agenda utilizando dicionário, a agenda deve ter uma lista de 3 contatos.
# 2. Os contatos, além do nome, devem possuir telefone e email.
agenda = {
    'contatos': [
        {'nome': 'alfa', 'tel': '12345678', 'email': 'alfa@alfa.com'},
        {'nome': 'beta', 'tel': '12341234', 'email': 'beta@beta.com'},
        {'nome': 'charlie', 'tel': '56785678', 'email': 'charlie@charlie.com'},
    ]
}


# 3. Verifique se há algum contato com o nome 'marcos'.
proc_nome = 'marcos'

for contato in agenda['contatos']:
    if proc_nome == contato['nome']:
        print(f'Há uma contato chamado: {proc_nome}')
        break


# 4. Altere o telefone do primeiro contato.
agenda['contatos'][0]['tel'] = '98765432'


# 5. calcule quanto contatos possuem na lista.
print(len(agenda['contatos']))
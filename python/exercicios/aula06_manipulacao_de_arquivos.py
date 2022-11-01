# Aula 06 - Manipulação de Arquivos

# 2. Crie um programa que leia um arquivo CSV;
# with open('./cadastro.csv', 'r') as arquivo_inicial:
#     linha = arquivo_inicial.readlines()
#     pass


try:
    with open('cadastro.csv', 'r') as file:
        lines = file.readlines()
        print(lines)
except:
    print('Erro no arquivo')


# 3. Processe o arquivo removendo o campo ID;
# 4. Grave o resultado em um novo arquivo.
linhas = []

for line in lines[1:]:
    linhas.append(line[2:])

with open('arquivo_gravado.txt', 'w', encoding='utf-8') as arquivo_escrita:
    for i in linhas:
        arquivo_escrita.write(i)
    arquivo_escrita.write('\n')

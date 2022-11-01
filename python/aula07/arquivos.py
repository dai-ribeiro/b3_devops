### ARQUIVOS

# 1. Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e
# gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos

# - O arquivo de entrada possui o seguinte formato:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256

# - O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4
#
# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5

IPs_invalidos = ['257.32.4.5\n', '85.345.1.2\n', '9.8.234.5\n']
invalidos = []

with open('IPs.txt', 'r') as arquivo_leitura, \
    open('IPs_saida.txt', 'w', encoding='utf-8') as arquivo_saida:

    linha = arquivo_leitura.readlines()

    arquivo_saida.write('[Endereços válidos:]\n')
    for item in linha:
        if item in IPs_invalidos:
            invalidos.append(item)
        else:
            arquivo_saida.write(item)

    arquivo_saida.write('\n\n[Endereços válidos:]\n')
    for i in invalidos:
        arquivo_saida.write(i)

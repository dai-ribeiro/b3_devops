### MÓDULOS

# 1. Crie um sistema modular que calcule área de 3 formas geométricas. O sistema deve conter:
#       a. um arquivo principal chamado 'main.py' contendo o menu do sistema.
#       b. o menu deve ter 4 opções: sendo as 3 primeiras para cálculo das formas geometricas e a última para
#          encerrar a execução
#       c. um móludo chamado 'geometria.py' contendo as fórmulas de cálculo das áreas

import geometria

print('*************************************')
print('********** CÁLCULO DA ÁREA **********')
print('*************************************')
print('De qual forma deseja calcular a área:')
print('1 - Triângulo')
print('2 - Círculo')
print('3 - Quadrado')
print('4 - Sair')
print('*************************************')

opcao = input('Digite a opcao desejada: ')

if opcao == '1':
    base = float(input('Informe o valor da base: '))
    altura = float(input('Informe o valor da altura: '))
    print(geometria.area_triang(base, altura))

elif opcao == '2':
    raio = float(input('Informe o valor do raio: '))
    print(geometria.area_circ(raio))

elif opcao == '3':
    lado = float(input('Informe o valor do lado: '))
    print(geometria.area_quadrado(lado))

elif opcao == '4':
    print('Programa finalizado')




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
#
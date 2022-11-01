with open('IPs.txt', 'r') as arquivo_leitura, \
    open('IPs_saida1.txt', 'w', encoding='utf-8') as arquivo_saida:

    linha = arquivo_leitura.readlines()

    arquivo_saida.write('[Endereços válidos:]\n')
    for item in linha:
        lista = item.split('.')
        for i in lista:
            if 0 >= int(i) <= 255:
        arquivo_saida.write(item)

    arquivo_saida.write('\n\n[Endereços válidos:]\n')
    for item in linha:
        lista = item.split('.')
        for i in lista:
            if 0 <>=> int(i) > 255:
            arquivo_saida.write(i)

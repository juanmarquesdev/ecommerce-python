def RealizarCompra():
    import csv, sys
    print('\nEstes são os produtos disponíveis:\n')
    nome_ficheiro = 'produtos-cadastrados.csv'
    with open(nome_ficheiro, 'r') as ficheiro:
        reader = csv.reader(ficheiro, delimiter = ';')
        for linha in reader:
            print(linha[1] + ' ' + linha[2] + ' ' + ' R$ ' + linha[3])
    
    cod = input('\nDigite o código do produto que deseja comprar: ')
    quant = int(input('\nDigite a quantidade: '))
    
    with open(nome_ficheiro, 'r') as ficheiro:
        reader = csv.reader(ficheiro, delimiter = ';')
        for linha in reader:
            if linha[1] == cod:
                print('\n Deseja realizar a compra do produto ' + linha[2])
                print('\n Com a quantidade de ' + str(quant) + ' sairá no valor de R$ ' + str((quant * float(linha[3]))))
    
    confir = int(input('\n Confirmar a compra?(1 para sim, qualquer numero para não): '))
    if confir == 1:
        with open('compras-realizadas.csv', 'a') as archive:
            with open(nome_ficheiro, 'r') as ficheiro:
                reader = csv.reader(ficheiro, delimiter = ';')
                for linha in reader:
                    if linha[1] == cod:
                        archive.write(linha[0] + ';' + linha[1] + ';' + linha[2] + ';' + linha[3] + ';' + str(quant) + ';' + str((quant * float(linha[3]))) + '\n')
        with open('ultima-compra.csv', 'w') as archive:
            with open(nome_ficheiro, 'r') as ficheiro:
                reader = csv.reader(ficheiro, delimiter = ';')
                for linha in reader:
                    if linha[1] == cod:
                        archive.write(linha[0] + ';' + linha[1] + ';' + linha[2] + ';' + linha[3] + ';' + str(quant) + ';' + str((quant * float(linha[3]))) + '\n')
        print('\n Compa realizada com sucesso!\n')
    else:
        print ('\n Voltando...\n')
        

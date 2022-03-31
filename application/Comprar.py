import RealizarCompra
import csv
def Comprar():
    number = 0
    while number == number:
        try:
            print('Estas são as opções disponíveis no Comprar: ')
            print(' 1 - Ofertas Disponíveis')
            print(' 2 - Novidades')
            print(' 3 - Comprar')
            print(' 4 - Voltar')
            number = int(input('\n Digite sua opção: '))
        except:
            print ('\n Algo deu errado, tente denovo.\n')
            number = 0

        if  number == 1:
            print ('\n Chamando opção 1...\n')
            
            file = open('descricao-oferta.txt', 'r')
            
            registro = file.readline()
            print('Esta é a Oferta de hoje: ')
            print(registro)
            
         
            sn = int(input('\n Deseja comprar o produto em oferta?(1 para sim e 0 para não): '))
            
            if sn == 1:
                quant = int(input('\nDigite a quantidade: '))
                with open('ofertas-disponiveis.csv', 'r') as ficheiro:
                    reader = csv.reader(ficheiro, delimiter = ';')
                    for linha in reader:
                        print('\n Deseja realizar a compra do produto ' + linha[2])
                        print('\n Com a quantidade de ' + str(quant) + ' sairá no valor de R$ ' + str((quant * float(linha[3]))))
                        
                confir = int(input('\n Confirmar a compra?(1 para sim, qualquer numero para não): '))
                if confir == 1: 
                    with open('compras-realizadas.csv', 'a') as archive:
                        with open('ofertas-disponiveis.csv', 'r') as ficheiro:
                            reader = csv.reader(ficheiro, delimiter = ';')
                            for linha in reader:
                                archive.write(linha[0] + ';' + linha[1] + ';' + linha[2] + ';' + linha[3] + ';' + str(quant) + ';' + str((quant * float(linha[3]))) + '\n')
                                
                print('\n Compa realizada com sucesso!\n')
                
            elif sn == 0:
                print ('\n Voltando...\n')
                break
                
            else:
                print('\n Opção inválida. Digite novamente.\n')
        
        elif  number == 2:
            print ('\n Chamando opção 2...\n')
            
            file = open('novidade.txt', 'r')
            
            registro = file.readline()
            print('Esta é a Novidade de hoje: ')
            print(registro)
            print('\n')
            
            
        elif  number == 3:
            print ('\n Chamando opção 3...\n')
            RealizarCompra.RealizarCompra()

        elif  number == 4:
            print ('\n Voltando...\n')
            break
            
        else:
            print('\n Opção inválida. Digite novamente.')
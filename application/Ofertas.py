def Ofertas():
    number = 0
    while number == number:
        try:
            print('Estas são as opções disponíveis no Ofertas: ')
            print(' 1 - Cadastrar nova oferta')
            print(' 2 - Voltar para Cadastro')
            
            number = int(input('\n Digite sua opção: '))
        except:
            print ('\n Algo deu errado, tente denovo.\n')
            number = 0
            
        if  number == 1:
            print ('\n Chamando opção 1...\n') 
            
            file1 = open('produtos-cadastrados.csv', 'r')
            print('Estes são os produtos cadastrados...\n')
            
            registro1 = file1.readline()
            while registro1:
                print(registro1)
                registro1 = file1.readline()
            
            oferta = input('Digite uma descrição para a oferta que deseja cadastrar: ')
            codtip = input('Digite o código do tipo de produto que deseja cadastrar: ')
            codprod = input('Digite o código do produto: ')
            produto = input('Digite o nome do produto correspondente: ')
            valor = input('Digite o preço do produto: ')
            
            
            descricaoOferta = open('descricao-oferta.txt', 'w')
            ofertaFile = open('ofertas-disponiveis.csv', 'w')
            
            ofertaFile.write(str(codtip) + ';' + str(codprod) + ';' + str(produto) + ';' + str(valor) + '\n')
            descricaoOferta.write(oferta)

            print('\n Oferta registrada!')
            print('Obs: Ao registrar uma nova oferta, a oferta anterior é apagada...\n')
            ofertaFile.close()
            descricaoOferta.close()
            
        elif  number == 2:
            print ('\n Voltando...\n')
            break

        else:
            print('\n Opção inválida. Digite novamente.')
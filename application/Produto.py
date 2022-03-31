def Produto():
    number = 0
    while number == number:
        try:
            print('Estas são as opções disponíveis no Produto: ')
            print(' 1 - Cadastrar novo produto')
            print(' 2 - Voltar para Cadastro')
            
            number = int(input('\n Digite sua opção: '))
        except:
            print ('\n Algo deu errado, tente denovo.\n')
            number = 0

        if  number == 1:
            print ('\n Chamando opção 1...\n') 
            
            file = open('tipos-cadastrados.csv', 'r')
            print('Estes são os tipos de produtos cadastrados...\n')
            
            registro = file.readline()
            while registro:
                print(registro)
                registro = file.readline()
            
            codtip = input('Digite o código do tipo de produto que deseja cadastrar: ')
            codprod = input('Digite o código do produto: ')
            produto = input('Digite o nome do produto correspondente: ')
            valor = input('Digite o preço do produto: ')
            
            arquivo1 = open('produtos-cadastrados.csv', 'r') # Abra o arquivo (leitura)
            conteudo1 = arquivo1.readlines()
            conteudo1.append(str(codtip) + ';' + str(codprod) + ';' + str(produto) + ';' + str(valor) + '\n')   # insira seu conteúdo

            arquivo1 = open('produtos-cadastrados.csv', 'w') # Abre novamente o arquivo (escrita)
            arquivo1.writelines(conteudo1)    # escreva o conteúdo criado anteriormente nele.
            arquivo1.close()
            
            print('\n Produto cadastrado com sucesso!\n')
            
        elif  number == 2:
            print ('\n Voltando...\n')
            break

        else:
            print('\n Opção inválida. Digite novamente.')
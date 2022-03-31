def Tipo():
    number = 0
    while number == number:
        try:
            print('Estas são as opções disponíveis no Tipo: ')
            print(' 1 - Cadastrar novo tipo')
            print(' 2 - Voltar para Cadastro')
            
            number = int(input('\n Digite sua opção: '))
        except:
            print ('\n Algo deu errado, tente denovo.\n')
            number = 0

        if  number == 1:
            print ('\n Chamando opção 1...\n') 
            
            tipoCod = input('Digite o código do tipo que deseja cadastrar: ')
            tipoProd = input('Digite o tipo de produto correspondente: ')
            
            arquivo = open('tipos-cadastrados.csv', 'r') # Abra o arquivo (leitura)
            conteudo = arquivo.readlines()
            conteudo.append(str(tipoCod) + ';' + str(tipoProd) + '\n')   # insira seu conteúdo

            arquivo = open('tipos-cadastrados.csv', 'w') # Abre novamente o arquivo (escrita)
            arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.
            arquivo.close()
            
            print('\n Tipo cadastrado com sucesso!\n')
            
        elif  number == 2:
            print ('\n Voltando...\n')
            break

        else:
            print('\n Opção inválida. Digite novamente.')

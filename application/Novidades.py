def Novidades():
    number = 0
    while number == number:
        try:
            print('Estas são as opções disponíveis no Novidades: ')
            print(' 1 - Cadastrar uma Novidade')
            print(' 2 - Voltar para Cadastro')
            
            number = int(input('\n Digite sua opção: '))
        except:
            print ('\n Algo deu errado, tente denovo.\n')
            number = 0
            
        if  number == 1:
            print ('\n Chamando opção 1...\n') 
            
            nov = input('Registre aqui uma novidade: ')
            
            novidade = open('novidade.txt', 'w')
            novidade.write(nov)

            print('\n Novidade registrada!')
            print('Obs: Ao registrar uma novidade nova, a anterior é apagada...\n')
            novidade.close()
            
        elif  number == 2:
            print ('\n Voltando...\n')
            break

        else:
            print('\n Opção inválida. Digite novamente.')
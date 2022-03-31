import Tipo
import Produto
import Ofertas
import Novidades

def Cadastro():
    number = 0
    while number == number:
        try:
            print('Estas são as opções disponíveis no Cadastro: ')
            print(' 1 - Tipo')
            print(' 2 - Produto')
            print(' 3 - Oferta ')
            print(' 4 - Novidade')
            print(' 5 - Voltar')
            number = int(input('\n Digite sua opção: '))
        except:
            print ('\n Algo deu errado, tente denovo.\n')
            number = 0

        if  number == 1:
            print ('\n Chamando opção 1...\n')
            Tipo.Tipo()

        elif  number == 2:
            print ('\n Chamando opção 2...\n')
            Produto.Produto()
            
        elif  number == 3:
            print ('\n Chamando opção 3...\n')
            Ofertas.Ofertas()
            
        elif  number == 4:
            print ('\n Chamando opção 4...\n')
            Novidades.Novidades()

        elif  number == 5:
            print ('\n Voltando...\n')
            break

        else:
            print('\n Opção inválida. Digite novamente.')
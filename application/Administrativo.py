import Cadastro
import csv
def Administrativo():
    number = 0
    while number == number:
        try:
            print('Estas são as opções disponíveis no Administrativo: ')
            print(' 1 - Cadastro')
            print(' 2 - Produtos Vendidos ')
            print(' 3 - Voltar ')
            number = int(input('\n Digite sua opção: '))
        except:
            print ('\n Algo deu errado, tente denovo.\n')
            number = 0

        if  number == 1:
            print ('\n Chamando opção 1...\n')
            Cadastro.Cadastro()

        elif  number == 2:
            print ('\n Chamando opção 2...\n')
            print('\n Estes são os produtos vendidos: \n')
            with open('compras-realizadas.csv', 'r') as compras:
                reader = csv.reader(compras, delimiter = ';')
                for linha in reader:
                    print(linha[4] + ' unidades de ' + linha[2])
            print('\n')

        elif  number == 3:
            print ('\n Voltando...\n')
            break

        else:
            print('\n Opção inválida. Digite novamente.')

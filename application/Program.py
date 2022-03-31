import Administrativo
import Comprar
import UltimasCompras

print('\n')
print('************************')
print('* BEM VINDO AO SISTEMA *')
print('************************')
print('\n')

number = 0

while number == number:
    try:
        print('Estas são as opções disponíveis: ')
        print(' 1 - Comprar ')
        print(' 2 - Últimas compras ')
        print(' 3 - Administrativo ')
        print(' 10 - Fim ')
        number = int(input('\n Digite sua opção: '))
    except:
        print ('\n Algo deu errado, tente denovo.\n')
        number = 0
        
    if number == 10:
        print('\n Obrigado por usar o sistema!')
        break
        
    if  number > 10:
        print('\n Opção inválida. Digite novamente.')
        
    elif  number == 1:
        print ('\n Chamando opção 1...\n')
        Comprar.Comprar()

    elif  number == 2:
        print ('\n Chamando opção 2...\n')
        UltimasCompras.UltimasCompras()

    elif  number == 3:
        print ('\n Chamando opção 3...\n')
        Administrativo.Administrativo()

    else:
        print('\n Opção ' + str(number) + ' ainda em desenvolvimento... ')
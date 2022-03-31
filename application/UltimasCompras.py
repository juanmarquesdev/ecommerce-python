def UltimasCompras():
    import csv
    print('\n Esta é a última compra realizada no sistema: \n')
    with open('ultima-compra.csv', 'r') as compras:
        reader = csv.reader(compras, delimiter = ';')
        for linha in reader:
            print(linha[4] + ' unidades de ' + linha[2])
    print('\n')
    
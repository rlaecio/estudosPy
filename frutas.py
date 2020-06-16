# coding: utf-8
frutas = ['Banana', 'Maca', 'Pera', 'Uva', 'Melancia', 'Jamelão']

frutaPedida = input('Qual é a fruta deseja consultar ?')

if(frutaPedida in frutas):
    print ('Sim, temos a fruta.')
else:
    print ('Não temos a fruta.')

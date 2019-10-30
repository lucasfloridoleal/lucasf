import os

p = float(input('Qual o preço da Lata ou Garrafa? '))
v = float(input('Qual o volume da Lata ou Garrafas?: '))

pl = (1000 / v) * p

if pl <= 6:

    print(f'O preço por Litro comprando a Lata ou Garrafa é {pl:.2f}', 'Reais\nShow de bola:)!!!')

elif pl <= 8:

    print(f'O preço por Litro comprando a Lata ou Garrafa é {pl:.2f}', 'Reais\nCarim!!!')

elif pl <= 10:

    print(f'O preço por Litro comprando a Lata ou Garrafa é {pl:.2f}', 'Reais\nCaro!!!')

else:
    print(f'O preço por Litro comprando a Lata ou Garrafa é {pl:.2f}', 'Reais\nCaro pra carai!!!')

os.system('pause')
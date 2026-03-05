dist = int(input('Qual a distância da viagem? '))
if dist <= 200:
    print('O valor da passagem é {}'.format(dist*0.5))
else:
    print('O valor da passagem é {}'.format(dist*0.45))
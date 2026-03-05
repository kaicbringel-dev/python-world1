vel = int(input('Digite a velocidade do carro: '))
n = vel - 80
if vel>=80:
    print('Você excedeu a velocidade máxima e foi multado!')
    print('A multa vai custar R$7 por cada km rodado')
    print('Multa: R${}'.format(n*7))
else:
    print('Abaixo da velocidade máxima. Pode seguir!')
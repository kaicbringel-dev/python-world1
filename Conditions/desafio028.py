import random

print('JOGO DA ADIVINHAÇÃO')
print('Tente adivinhar o número que eu escolhi!')
lista = [0, 1, 2, 3, 4, 5]
n = random.choice(lista)
resp = int(input('Digite o número que eu pensei: '))
if resp == n:
    print('Você acertou! O número que eu escolhi foi {}'.format(n))
else:
    print('Você errou! O número que eu escolhi foi {}'.format(n))
print('Fim de jogo')
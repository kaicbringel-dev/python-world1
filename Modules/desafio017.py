from math import sqrt, hypot
ca = int(input('Digite o Cateto Adjacente: '))
co = int(input('Digite o Cateto Oposto: '))
#print('A hipotenusa do triângulo retângulo com os catetos {} e {} é {}.'.format(ca, co, sqrt((ca*ca)+(co*co))))
print('A hipotenusa do triângulo retângulo com os catetos {} e {} é {}.'.format(ca, co, hypot(ca, co)))
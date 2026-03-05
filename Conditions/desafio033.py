n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
if n1 > n2 and n1 >n3:
    print('O maior valor é {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior valor é {}'.format(n2))
elif n3 > n1 and n3 > n2:
    print('O maior valor é {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('O menor valor é {}'.format(n1))
elif n2 < n1 and n2 <n3:
    print('O menor valor é {}'.format(n2))
elif n3 < n1 and n3 < n2:
    print('O menor valor é {}'.format(n3))
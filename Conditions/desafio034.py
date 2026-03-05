sal = int(input('Qual é o salário do funcionário? '))
if sal > 1250:
    print('Quem ganhava R${:.2f} passa a ganhar {:.2f} agora.'.format(sal, (sal*0.1)+sal))
else:
    print('Quem ganhava R${:.2f} passa a ganhar {:.2f} agora.'.format(sal, (sal*0.15)+sal))
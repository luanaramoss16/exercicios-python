salario = float(input('Informe aqui o salário do funcionário: R$ '))
reajuste = salario * 0.15
print('O salário atual do funcionário é de {:.1f}. Com o reajuste de 15%, este passa a ser {:.1f}'.format(salario, salario + reajuste))
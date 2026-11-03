#calculo de aumento salarial
#crie um programa que solicite o salario atual de um funcionario. em seguida, calcule um aumento de 15% sobre o salario
#apresente o valor do aumento e o novo salario do funcionario apos o reajuste

salario = float(input('informe o salario atual: '))
percentual = float(input('informe o percentual: '))

percentual = percentual / 100

aumento = salario * percentual
total_aumento = salario + aumento

print(f'\nsalario anterior {salario}')
print(f'reajuste de: {aumento:.2f}')
print(f'novo salario: {total_aumento}')
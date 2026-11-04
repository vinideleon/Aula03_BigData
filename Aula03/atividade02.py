#Crie um algoritmo que receba dois números e apresente na tela os resultados das operações de 
# soma, subtração, multiplicação e divisão.

numero_1 = float(input('informe o seu primeiro numero: '))
numero_2 = float(input('informe o seu segundo numero: '))

soma = numero_1 + numero_2
subtração = numero_1 - numero_2
multiplicação = numero_1 * numero_2
divisão = numero_1 / numero_2

print(f'a soma dos numeros é: {soma:.1f}')

print(f'a subtração dos numeros é: {subtração:.1f}')

print(f'a multiplicação dos numeros é: {multiplicação:.1f}')

print(f'a divisão dos numeros é: {divisão:.1f}')
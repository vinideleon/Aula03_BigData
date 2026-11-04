#crie um algoritmo que receba duas notas de um aluno, calcule a media final e apresente na tela as duas notas 
# e as media obtida

Primeira_nota = float(input('informe a sua primeira nota: '))
segunda_nota = float(input('informe a sua segunda nota: '))

Nota_total = Primeira_nota + segunda_nota
media_final = Nota_total / 2 

print(f'sua media é: {media_final:.2f} ')
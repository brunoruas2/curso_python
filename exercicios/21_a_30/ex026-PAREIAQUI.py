# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes 
# aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a 
# última vez.

#frase = input('Digite uma Frase: ').strip()
frase = 'Amanda ama Pedro'
frase = frase.upper()

print('A letra "a" aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra "a" apareceu na posição {}'.format(frase.find('A')))
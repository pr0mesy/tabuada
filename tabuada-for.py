# Atividade 01:
# Tabuada de um Número:
# Faça um programa que solicite um número ao usuário e use
# um laço for para exibir a tabuada desse número (de 1 a 10).

numero = int(input('Digite um número para ver sua tabuada: '))

for i in range (1, 11):
    resultado = numero * i
    print(f'{numero} * {i} = {resultado}')
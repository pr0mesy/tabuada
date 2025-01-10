# Atividade 03:
# Tabuada de um Número:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10).

numero = int(input('Digite um número para ver sua tabuada. '))
multiplicador = 1

while multiplicador <= 10:
    resultado = numero * multiplicador
    print(f'{numero} * {multiplicador} = {resultado}')
    multiplicador += 1
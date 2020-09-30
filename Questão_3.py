"""
3 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um valor
válido. (2,0)
"""

while True:

    nota = int(input("Digite uma nota: "))

    if nota < 0 or nota > 10:
        print("Nota inválida. Tente novamente.")

    else:
        print("Nota digitada: ", nota)
        break
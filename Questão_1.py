"""1 - Darth Vader achou que seu exército de stormtrooper estava prendendo poucos
rebeldes, então lhe contratou para desenvolver um programa que leia um conjunto
indeterminado de número de refém presos por mês. Ao final da listagem informe o
menor e o maior número de capturados, a média e o valor mais próximo a média (não
utilize funções prontas do python). (2.0)"""

lista=[]
soma = 0
menor_capturados = 999
maior_capturados = 0
resposta = 0

while resposta != -1:

    num_refens = int(input("Insira o número de refens (-1 para sair): "))
    soma += num_refens
    lista.append(num_refens)

    if (num_refens < menor_capturados):
        menor_capturados = num_refens
        
    if (num_refens > maior_capturados):
        maior_capturados = num_refens

    if num_refens == -1:
        print("Programa terminado.")
        break

    print ("Menor número: ", menor_capturados)
    print ("Maior número: ", maior_capturados)
    print ("Prisioneiros capturados por vez: ", lista)
    print ("Média: ", soma/len(lista))
    print ("Número mais próximo da média: ", )

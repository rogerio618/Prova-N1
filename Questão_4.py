"""4 - Expliquei o que é decorator e padrões de projeto. Crie um decorator que mostre
o tempo de execução de uma função que soma 4 números aleatórios. (2,0)"""

"""Decorator é um padrão de projeto de software que permite
  adicionar um comportamento a um objeto já existente em tempo de execução, ou seja,
  agrega dinamicamente responsabilidades adicionais a um objeto.
  Decorators oferecem uma alternativa flexível ao uso de herança para estender uma funcionalidade, com isso adiciona-se
  uma responsabilidade ao objeto e não à classe."""

import time

# Define decorator
def sistema(funcao):
    def wrapper():
        "Calcula o tempo de execução"
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        # Formata a mensagem que será mostrada na tela
        print("[{funcao}] Tempo total de execução: {tempo_total}".format(
            funcao=funcao.__name__,
            tempo_total=str(tempo_final - tempo_inicial))
        )

    return wrapper

# Decora a função com o decorator
@sistema
def digita_numero():
    numeros_somados=[]
    for n in range(4):
        numeros_somados.append(int(input("Digite um número: ")))
    print("A soma dos 4 números é igual a: ", sum(numeros_somados))

digita_numero()

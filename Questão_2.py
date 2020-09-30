"""2 - Crie um classe Funcionário com os atributos nome, idade e salário. Deve ter
um método aumenta_salario. Crie duas subclasses da classe funcionário,
programador e analista, implementando o método nas duas subclasses. Para
o programador some ao atributo salário mais 20 e ao analista some ao salário
mais 30, mostrando na tela o valor. Depois disso, crie uma classe de testes
instanciando os objetos programador e analista e chame o método
aumenta_salario de cada um.(2,0)"""

class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.aumento = 0

    def aumenta_salario(self):
        self.salario = self.salario + self.aumento


class Programador(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 20


class Analista(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 30

class Lider(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 666


p1 = Programador("Romualdo", 33, 100)
print("Funcionario: ",p1.nome)
print("Salario atual: ",p1.salario)
p1.aumenta_salario()
print("Salario com acrecimo: ",p1.salario)

a1 = Analista("João", 67, 10500)
print("Funcionario: ",a1.nome)
print("Salario atual: ",a1.salario)
a1.aumenta_salario()
print("Salario com acrecimo: ",a1.salario)

d6 = Lider("Satã", 666, "Almas")
print(d6.nome)
print('Recebe em ',d6.salario)
print('Satã tem almas o PIB de almas aumentando diariemente')

"""
    Leandro Marson Ribeiro RA: 20180666
    Wesley Albino dos Santos RA: 20181492
"""

class Cachorro:
    #metodo construtor
    def __init__(self, nome, data_nascimento, raca, sexo, cor_pelo):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.raca = raca
        self.sexo = sexo
        self.cor_pelo = cor_pelo

    #metodos
    def printando(self):
        print("Nome: {0}\nData de Nascimento: {1}\nRaça: {2}\nSexo: {3}\nCor do Pelo: {4}\n".format(self.nome, self.data_nascimento, self.raca, self.sexo, self.cor_pelo))

    def latir(self):
        print("Au au au\n")

    def enterrar_osso(self):
        print("{0} está enterrando o osso\n".format(self.nome))

#fim da classe

#instanciando objeto
dog = Cachorro("Bistéca","30/02/2010","Vira-Lata","Macho","Preto")

#chamando métodos
dog.printando()
dog.latir()
dog.enterrar_osso()

#fim do programa






    

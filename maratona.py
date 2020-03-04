"""
    Leandro Marson Ribeiro RA: 20180666
    Wesley Albino dos Santos RA: 20181492
"""

from random import randint

class Participante:
    #metodo construtor
    def __init__(self, nome):
        self.nome = nome
        self.vitorias = 0

    #metodos
    def status(self):
        print("Nome: {0}\nVitórias: {1}\n".format(self.nome, self.vitorias))
        

    def ganhar_maratona(self):
        self.vitorias = self.vitorias+1
        print("{0} ganhou a maratona!\nVitórias: {1}\n".format(self.nome, self.vitorias))

#fim da classe
        
class Maratona:
    #metodo construtor
    def __init__(self, descricao, data, hora, local_inicio, local_fim):
        self.descricao = descricao
        self.data = data
        self.hora = hora
        self.local_inicio = local_inicio
        self.local_fim = local_fim
        self.participantes = []

    #metodos
    def status(self):
        print("------------------\nDescrição: {0}\nData: {1}\nHora: {2}\nLocal de Início: {3}\nLocal de Fim: {4}\n".format(self.descricao, self.data, self.hora, self.local_inicio, self.local_fim))
        print("Participantes: \n")
        for x in self.participantes:
            print(x.nome)
            
        print("\n------------------\n")


    def iniciar_maratona(self):
        print ("Maratona iniciada!...\n")
        random = randint(0, len(self.participantes))
        self.participantes[random].ganhar_maratona()
        

    def cadastrar_participante(self, participante):
        self.participantes.append(participante)
        print("------------------\nParticipante cadastrado!\nNúmero de participantes: {0}\n".format(len(self.participantes)))
        participante.status()
        print("------------------\n")

#fim da classe

#instanciando objetos
p = []
p.append(Participante("João"))#utilizando o metodo append() para adicionar um Participante no vetor p[]
p.append(Participante("Lucas"))
p.append(Participante("Mathias"))
p.append(Participante("Daives"))
p.append(Participante("Hugo"))

mr = Maratona("Maratona Americanense","27/10/2020","07:30","R. das Laranjeiras","Av. Solimões")

#chamando métodos dos participantes
for x in p:
    print(x.status())


#chamando métodos da maratona
for x in p:#cadastrando todos os participantes
    mr.cadastrar_participante(x)

mr.iniciar_maratona()
mr.status()




        

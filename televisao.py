"""
    Leandro Marson Ribeiro RA: 20180666
    Wesley Albino dos Santos RA: 20181492
"""

class Televisao:
    #metodo construtor
    def __init__(self, marca, cor, tipo_tela):
        self.marca = marca
        self.cor = cor
        self.tipo_tela = tipo_tela
        self.ligada = False
        self.canal = 0
        self.volume = 50

    #metodos
    def abrir_menu(self):
        if(self.ligada==True):
            print("Marca: {0}\nCor: {1}\nTipo da Tela: {2}\nVolume: {3}\nCanal: {4}\n".format(self.marca, self.cor, self.tipo_tela, self.volume, self.canal))
        else:
            print("Televisão está desligada!\n")


    def ligar(self):
        if(self.ligada==False):
            self.ligada=True
            print("Ligando...\n")
        else:
            print("A televisão já está ligada!\n")


    def desligar(self):
        if(self.ligada==True):
            self.ligada=False
            print("Desligando...\n")
        else:
            print("A televisão já está desligada!\n")


    def mudo(self):
        self.volume=0
        print("Mudo\n")


    def aumentar_volume(self):
        if(self.volume<=100):
            self.volume = self.volume+10
            print("Volume: {0}\n".format(self.volume))
        else:
            print("Volume já está no máximo!\n")


    def diminuir_volume(self):
        if(self.volume>0):
            self.volume = self.volume-10
            print("Volume: {0}\n".format(self.volume))
        else:
            print("Volume já está no mínimo!\n")


    def mudar_canal(self,canal):
        self.canal = canal
        print("Mudando para o canal {0}...\n".format(self.canal))
        
#fim da classe

#instanciando objeto
tv = Televisao("Sansung","Cinza","LCD")

#chamando métodos
tv.ligar()
tv.abrir_menu()
tv.aumentar_volume()
tv.diminuir_volume()
tv.mudo()
tv.aumentar_volume()
tv.mudar_canal(15)
tv.abrir_menu()
tv.desligar()

#fim do programa











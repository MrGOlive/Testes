class Personagem:
    def __init__(self, nome, vida, defesa):
        self.nome = nome
        self.vida = vida
        self.defesa = defesa
        self.vida_maxima = 100

    def receber_dano(self, ataque_inimigo):
        dano_real = max(0, ataque_inimigo - self.defesa) 
        self.vida = self.vida - dano_real
        print(f"{self.nome} recebeu {dano_real} de dano! Vida restante: {self.vida}")

    def curar(self, quantidade):
        self.vida = self.vida + quantidade
        if self.vida > 100:
            self.vida = 100
            print(f"O personagem usou uma cura de {quantidade}, ele ficou com o máximo de {self.vida} de vida!")
        print(f"O personagem se curou em {quantidade} e foi para {self.vida} de vida!")
    
    def is_vivo(self):
        if self.vida <= 0:
            print("O personagem morreu!")

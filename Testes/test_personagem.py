import unittest
from personagem import Personagem

class TestPersonagem(unittest.TestCase):
    # Solução Ágil (QA automatizado)
    def test_receber_dano_ataque_menor_que_defesa(self):

        heroi = Personagem("Paladino", vida=100, defesa=50)
        
        heroi.receber_dano(60)

    def test_curar_nao_deve_ultrapassar_vida_maxima(self):
        heroi = Personagem("Mago", vida = 100, defesa = 10)
        heroi.receber_dano(40)
        heroi.curar(10)
    
    def test_dano_fatal_deve_matar_personagem(self):
        heroi = Personagem("Ladino", vida = 100, defesa = 5)
        heroi.receber_dano(105)
        heroi.is_vivo()

if __name__ == '__main__':
    unittest.main()
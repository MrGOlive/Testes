from personagem import Personagem

# Simulação do problema em sala:
heroi = Personagem("Guerreiro", vida=100, defesa=50)
heroi.receber_dano(200) # Ataque fraco (menor que a defesa)
# Resultado: O herói é curado em 30 pontos de vida!
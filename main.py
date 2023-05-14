from barra import *
from bola import *

import time

############################################
# Função
def start_game(event):

    # Variáveis
    global lost, count
    lost = False
    count = 0

    # Chamada à função
    score()

    # Variável que recebe o resultado da função
    canvas.itemconfig(game, text=" ")

    # Métodos dos objetos
    time.sleep(1)
    Barra.draw()
    Bola.draw()

# Instâncias dos objetos Barra e Bola
Barra = Barra(canvas, "olive")
Bola = Bola(canvas, Barra, "white")

# Variáveis que recebem o resultado das funções
canvas.bind_all("<Button-1>", start_game)

# Executa o programa
root.mainloop()



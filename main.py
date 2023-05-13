from Janela import *
from Barra import *
from Bola import *

######################################

def start_game(event):
    global lost
    barra.draw()

barra = Barra(canvas, length)
bola = Bola(canvas, Barra)
canvas.bind_all("<Button-1>", start_game)

root.mainloop()

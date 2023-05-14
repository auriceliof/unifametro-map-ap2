import time

from janela import *
from barra import *
from bola import *

######################################

def start_game(event):
    global lost
    time.sleep(1)
    bola.draw()
    barra.draw()


barra = Barra(canvas, length)
bola = Bola(canvas, Barra)
canvas.bind_all("<Button-1>", start_game)

root.mainloop()

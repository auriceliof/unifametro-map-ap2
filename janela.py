from barra import *
from bola import *

from tkinter import *
import time
from PIL import Image, ImageTk


# Instância do Objeto Tk
root = Tk()
root.title("Ping Pong")
root.resizable(0,0)
root.wm_attributes("-topmost", 1)

# Variável recebendo o resultado da função Canvas
canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
canvas.pack()

background_image_path = "BGImage.png"  # Substitua pelo caminho da sua imagem de fundo
bg_image = Image.open(background_image_path)
bg_photo = ImageTk.PhotoImage(bg_image)

canvas.create_image(0, 0, image=bg_photo, anchor=NW)

root.update()

# Variável
count = 0

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

# Função
def score():
    canvas.itemconfig(score_now, text="Você acertou " + str(count) + "x")

# Função
def game_over():
    canvas.itemconfig(game, text="Game over!")

# Instâncias dos objetos Barra e Bola
Barra = Barra(canvas, "olive")
Bola = Bola(canvas, Barra, "white")

# Variáveis que recebem o resultado das funções
score_now = canvas.create_text(370, 20, text="Você acertou " + str(count)+ "x", fill = "lime", font=("Arial", 20))
game = canvas.create_text(400, 300, text=" ", fill="white", font=("Arial", 40))
canvas.bind_all("<Button-1>", start_game)

# Executa o programa
root.mainloop()



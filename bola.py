import random
from tkinter import *
from PIL import Image, ImageTk
#######################################################


# Variável
count = 0

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
def score():
    canvas.itemconfig(score_now, text="Você acertou " + str(count) + "x")

# Função
def game_over():
    canvas.itemconfig(game, text="Game over!")
#######################################################


class Bola:
    def __init__(self, canvas, Barra, color):

        # Variáveis
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        # Lista
        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        # Variáveis
        self.x = starts_x[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    # Função
    def draw(self):

        # Variáveis
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        # Condicional if
        if pos[1] <= 0:
            # Variável
            self.y = 3

        # Condicional if
        if pos[3] >= self.canvas_height:
            # Variável
            self.y = -3

        # Condicional if
        if pos[0] <= 0:
            # Variável
            self.x = 3

        # Condicional if
        if pos[2] >= self.canvas_width:
            # Variável
            self.x = -3

        # Variável
        self.Barra_pos = self.canvas.coords(self.Barra.id)

        # Condicional if aninhado
        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                # Variáveis
                self.y = -3
                global count
                count += 1

                # Chamada à função
                score()

        # Condicional if
        if pos[3] <= self.canvas_height:

            # Variável
            self.canvas.after(10, self.draw)
        else:

            # Chamada à função
            game_over()

            # Variáveis
            global lost
            lost = True

# Variáveis que recebem o resultado das funções
game = canvas.create_text(400, 300, text=" ", fill="white", font=("Arial", 40))
score_now = canvas.create_text(370, 20, text="Você acertou " + str(count)+ "x", fill = "lime", font=("Arial", 20))
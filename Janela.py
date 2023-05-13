import random
from tkinter import *
from PIL import Image, ImageTk

######################################################
# VARIÁVEIS

# Largura da barra
length = 300

# Velocidade da barra
speed = 7

# ?
lost = False

# Contagem
count = 0

######################################################

# Instâncias do Objeto Tk
root = Tk()
root.title("Ping Pong")
root.iconbitmap("Pokeball.ico")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)

# Recebendo o resultado da função Canvas
canvas = Canvas(root, width=800, height=600, bd=0, highlightthickness=0)
canvas.pack()

#PEGAR A IMAGEM
bg_image = Image.open("Image-BG.png")

#CONVERTER IMAGEM PARA TK
bg_photo = ImageTk.PhotoImage(bg_image)

#JOGAR A IMAGEM PARA DENTRO DO CANVAS
canvas.create_image(0, 0, image=bg_photo, anchor=NW)

# ATUALIZAR
root.update()

# CLASSE BARRA ###############################################################
class Barra:

    # CONSTRUTOR
    def __init__(self, canvas, length):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill="blue")
        self.canvas.move(self.id, 200, 400)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        self.position = self.canvas.coords(self.id)

        if self.position[0] <= 0:
            self.x = 0

        if self.position[2] >= self.canvas_width:
            self.x = 0

        global lost

        # VELOCIDADE DA BARRA
        if lost == False:
            self.canvas.after(speed, self.draw)
    def move_left(self, event):
        if self.position[0] >= 0:
            self.x = -3


    def move_right(self, event):
        if self.position[0] <= self.canvas_width:
            self.x = 3


# CLASSE BOLA ###############################################################
class Bola:
    def __init__(self, canvas, barra):
        self.canvas = canvas
        self.canvas = canvas
        self.barra = barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill="white")
        self.canvas.move(self.id, 245, 200)

        #POSIÇÃO DA BOLA (ESQUERDA X DIREITA)
        starts_x = [-3, -2, -1, 1, 2, 3]

        random.shuffle(starts_x)

        self.x = starts_x[0]

        #DIREÇÃO INICIAL DA BOLA (- = CIMA)
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        self.position = self.canvas.coords(self.id)

        if self.position[2] <= 0:
            self.y = 3

        if self.position[3] >= self.canvas_height:
            self.y = -3

        if self.position[0] <= 0:
            self.x = 3

        if self.position[1] >= self.canvas_width:
            self.x = -3


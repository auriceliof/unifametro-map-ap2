from tkinter import *
import time
from PIL import Image, ImageTk

root = Tk()
root.title("Ping Pong")
root.iconbitmap("Pokeball.ico")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)

canvas = Canvas(root, width=800, height=600, bd=0, highlightthickness=0)
canvas.pack()

#PEGAR A IMAGEM
bg_image = Image.open("Image-BG.png")

#CONVERTER IMAGEM PARA TK
bg_photo = ImageTk.PhotoImage(bg_image)

#JOGAR A IMAGEM PARA DENTRO DO CANVAS
canvas.create_image(0, 0, image=bg_photo, anchor=NW)

root.update()


# CLASSE BARRA

length = 500
lost = False
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

        if self.position[2] >= self.canvas_width :
            self.x = 0

        global lost

        if lost == False:
            self.canvas.after(10, self.draw)
    def move_left(self, event):
        if self.position[0] >= 0:
            self.x = -3


    def move_right(self, event):
        if self.position[0] <= self.canvas_width:
            self.x = 3


# CLASSE BOLA
class Bola:
    def __init__(self, canvas):
        self.canvas = canvas

def start_game(event):
    global lost
    lost = False
    time.sleep(1)
    barra.draw()

barra = Barra(canvas, length)
canvas.bind_all("<Button-1>", start_game)

root.mainloop()

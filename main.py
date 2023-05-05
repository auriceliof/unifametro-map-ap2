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
canvas.create_image(0, 0, image=bg_photo)


root.update()

root.mainloop()


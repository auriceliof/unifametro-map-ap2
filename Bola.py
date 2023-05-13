import random

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


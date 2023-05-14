
# Variável recebendo o valor digitado pelo usuário
level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))

# Variável
length = 300/level
lost = False

##############################################################
class Barra:
    def __init__(self, canvas, color):

        # Variáveis
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    # Função
    def draw(self):

        # Chamada ao método
        self.canvas.move(self.id, self.x, 0)

        # Variável
        self.pos = self.canvas.coords(self.id)

        # Condicional if
        if self.pos[0] <= 0:
            # Variável
            self.x = 0

        # Condicional if
        if self.pos[2] >= self.canvas_width:
            # Variável
            self.x = 0

        global lost

        # Condicional if
        if lost == False:
            self.canvas.after(10, self.draw)

    # Função

    def move_left(self, event):

        # Condicional if
        if self.pos[0] >= 0:
            # Variável
            self.x = -3

    # Função
    def move_right(self, event):

        # Condicional if
        if self.pos[2] <= self.canvas_width:
            # Variável
            self.x = 3
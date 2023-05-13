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
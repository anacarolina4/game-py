import random

class Player():
  def __init__(self, username: str, color: str = 'yellow'):
    self.x = random.randint(0, 800)
    self.y = random.randint(0, 600)
    self.speed = 10
    self.width = 1
    self.height = 1
    self.color = color
    self.name = username


# __init__ --> Quem inicializa, determina os valores iniciais da instância
# self --> Define um valor como ATRIBUTO da instância

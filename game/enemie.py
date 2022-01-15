import random

class Enemie():
  def __init__(self):
    self.x = random.randint(0, 800)
    self.y = random.randint(0, 600)
    self.width = 1
    self.height = 1
    self.color = '#aa0000'
    self.name = 'Enemie_'+str(random.randint(1000, 9999))

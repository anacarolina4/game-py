from pygame import display

class GameScreen():
  def __init__(self, gameName: str, width: int = 800, height: int = 600):
    self.gameName = gameName
    self.width = width
    self.height = height

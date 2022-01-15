import pygame

from game.screen import GameScreen
from game.player import Player
from game.enemie import Enemie



pygame.init()

GameWindow = GameScreen('Joguinho fodinha')
player = Player('Ana144hz')
enemie = Enemie()

screen = pygame.display.set_mode((GameWindow.width, GameWindow.height))

pygame.display.set_caption(GameWindow.gameName)

green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('https://kauefraga.vercel.app', True, green, blue)
textRect = text.get_rect()
textRect.center = (GameWindow.width // 2, GameWindow.height // 2)

# Render loop
while True:
  pygame.time.delay(50)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()

    commands = pygame.key.get_pressed()
    if commands[pygame.K_UP]:
      player.y -= player.speed
    if commands[pygame.K_DOWN]:
      player.y += player.speed
    if commands[pygame.K_LEFT]:
      player.x -= player.speed
    if commands[pygame.K_RIGHT]:
      player.x += player.speed

  # screen.blit(background, (0,0))
  screen.fill((0,0,0)) # Preenche a tela de preto (cor padrão)

  pygame.draw.circle(screen, player.color, (player.x, player.y), 50) # Desenha o player
  pygame.draw.circle(screen, enemie.color, (enemie.x, enemie.y), 50)

  screen.blit(text, textRect)

  #
  # Colisão / Collision
  #

  pygame.display.update() # Atualiza a tela, faz o fill() e o draw() novamente

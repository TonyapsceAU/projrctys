import pygame
import math
from pygame.locals import *
from block import Block

digits = 2
windowWidth = 400
windowHeight = 300

count = 0

def setup(digits):
  block1 = Block((windowWidth / 4) * 1, 0, 20, 1, 0, 0)
  m2 = pow(100, digits - 1)
  timeSteps = int(math.pow(10, (digits - 1)))
  block2 = Block((windowWidth / 4) * 3, 0, 100, m2, -1 / timeSteps, 20)
  return block1, block2, timeSteps


def write_to_file(filename, content):
  with open(filename, 'a') as file:
    file.write(str(content))
    file.write("\n")


pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()


def write_text(screen, object):
  font = pygame.font.Font(None, 36)  # Example font and size
  text_color = (255, 255, 255)  # Example text color (white)
  text_content = str(object.m)
  unicode_text = text_content.encode('utf-8')
  text_surface = font.render(unicode_text, True, text_color)
  screen.blit(text_surface, (object.x, object.y))


running = True
block1, block2, timeSteps = setup(digits)
while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = False
    elif event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        running = False

  screen.fill((255, 255, 255))

  for i in range(0, timeSteps):
    if (block1.collide(block2)):
      v1 = block1.bounce(block2)
      v2 = block2.bounce(block1)
      block1.v = v1
      block2.v = v2
      count += 1

    if (block1.hitWall()):
      block1.reverse()
      count += 1

    block1.update()
    block2.update()

  fill, rect = block1.show()
  pygame.draw.rect(screen, fill, rect)
  write_text(screen, block1)

  fill, rect = block2.show()
  pygame.draw.rect(screen, fill, rect)
  write_text(screen, block2)

  if ((block2.v > 0) and (block2.v > abs(block1.v))):
    print(digits, count)
    digits += 1
    block1, block2, timeSteps = setup(digits)
    count = 0

  # write_to_file("print.txt", (digits, count))
  clock.tick(60)
  pygame.display.update()

# Quit Pygame
pygame.quit()

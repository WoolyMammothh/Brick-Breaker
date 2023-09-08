import pygame
import os

BLACK, WHITE = (0, 0, 0), (255, 255, 255)
WIDTH, HEIGHT = 1000, 600
CHAR_HEIGHT, CHAR_WIDTH = 50, 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# paddle = pygame.draw.rect(screen, WHITE, (100, 50))
char_image = pygame.image.load(os.path.join('Assets', 'character.png'))
character = pygame.transform.scale(char_image, (CHAR_WIDTH, CHAR_HEIGHT))

def update_display(pink):
  screen.fill(BLACK)
  screen.blit(character, (pink.x, pink.y))
  pygame.display.update()

def main():
  pink = pygame.Rect((WIDTH//2)-(CHAR_WIDTH//2), (HEIGHT//2)-(CHAR_HEIGHT//2), 
                     CHAR_WIDTH, CHAR_HEIGHT)
  fps = pygame.time.Clock()
  running = True
  while running:
    fps.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    update_display(pink)

  pygame.quit()

if __name__ == "__main__":
  main()
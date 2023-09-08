import pygame
import os

BLACK, WHITE = (0, 0, 0), (255, 255, 255)
WIDTH, HEIGHT = 1000, 600
CHAR_HEIGHT, CHAR_WIDTH = 50, 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# paddle = pygame.draw.rect(screen, WHITE, (100, 50))
char_image = pygame.image.load(os.path.join('Assets', 'character.png'))
guy = pygame.transform.scale(char_image, (CHAR_WIDTH, CHAR_HEIGHT))

def update_display():
  screen.fill(BLACK)
  screen.blit(guy, ((WIDTH//2)-(CHAR_WIDTH//2), (HEIGHT//2)-(CHAR_HEIGHT//2)))
  pygame.display.update()

def main():
  fps = pygame.time.Clock()
  running = True
  while running:
    fps.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    update_display()

  pygame.quit()

if __name__ == "__main__":
  main()
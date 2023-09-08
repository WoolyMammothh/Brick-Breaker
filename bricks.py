import pygame

BLACK = (0, 0, 0)
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def update_display():
  screen.fill(BLACK)
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
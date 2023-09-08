import pygame
import os

BLACK, WHITE = (0, 0, 0), (255, 255, 255)
WIDTH, HEIGHT = 1000, 600
CHAR_HEIGHT, CHAR_WIDTH = 50, 50
SPEED = 8
BULLET_SPEED = 12
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# paddle = pygame.draw.rect(screen, WHITE, (100, 50))
char_image = pygame.image.load(os.path.join('Assets', 'character.png'))
character = pygame.transform.scale(char_image, (CHAR_WIDTH, CHAR_HEIGHT))
bullet_pic = pygame.image.load(os.path.join('Assets', 'bullet.png'))
clown = pygame.transform.scale(bullet_pic, (15, 15))


def update_display(pink, bullets):
  screen.fill(BLACK)
  screen.blit(character, (pink.x, pink.y))

  for bullet in bullets:
    pygame.draw.rect(screen, BLACK, bullet)
    screen.blit(clown, bullet)

  pygame.display.update()

def handle_movement(pink):
  keys_pressed = pygame.key.get_pressed()
  if keys_pressed[pygame.K_RIGHT] and pink.x + CHAR_WIDTH <= WIDTH:
    pink.x += SPEED
  if keys_pressed[pygame.K_LEFT] and pink.x >= 0:
    pink.x -= SPEED
  if keys_pressed[pygame.K_UP] and pink.y >= 0:
    pink.y -= SPEED
  if keys_pressed[pygame.K_DOWN] and pink.y + CHAR_HEIGHT <= HEIGHT:
    pink.y += SPEED



def shoot_bullets(bullets):
  for bullet in bullets:
      bullet.x += 20
      if bullet.x >= WIDTH:
        bullets.remove(bullet)


def main():
  pink = pygame.Rect((WIDTH//2)-(CHAR_WIDTH//2), (HEIGHT//2)-(CHAR_HEIGHT//2), 
                     CHAR_WIDTH, CHAR_HEIGHT)
  fps = pygame.time.Clock()
  running = True
  bullets = []
  while running:
    fps.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          bullet = pygame.Rect(pink.x + CHAR_WIDTH, pink.y + 15, 1, 1)
          bullets.append(bullet)
          
    shoot_bullets(bullets, pink)

    handle_movement(pink)

    update_display(pink, bullets)

  pygame.quit()

if __name__ == "__main__":
  main()
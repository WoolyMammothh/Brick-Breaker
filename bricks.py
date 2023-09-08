import pygame
import os

BLACK, WHITE = (0, 0, 0), (255, 255, 255)
WIDTH, HEIGHT = 1000, 600
CHAR_HEIGHT, CHAR_WIDTH = 50, 50
SPEED = 8
BULLET_SPEED = 12
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# paddle = pygame.draw.rect(screen, WHITE, (100, 50))

#CHARACTERS
char1_image = pygame.image.load(os.path.join('Assets', 'character.png'))
character = pygame.transform.scale(char1_image, (CHAR_WIDTH, CHAR_HEIGHT))
char2_image = pygame.image.load(os.path.join('Assets', 'character2.png'))
charactersized = pygame.transform.scale(char2_image, (CHAR_WIDTH, CHAR_HEIGHT))
character2 = pygame.transform.flip(charactersized, True, False)
  

#BULLETS
bullet_pic = pygame.image.load(os.path.join('Assets', 'child.png'))
child = pygame.transform.scale(bullet_pic, (15, 15))


def update_display(pink, green, bullets):
  screen.fill(BLACK)
  screen.blit(character, (pink.x, pink.y))
  screen.blit(character2, (green.x, green.y))

  for bullet in bullets:
    pygame.draw.rect(screen, BLACK, bullet)
    screen.blit(child, bullet)

  pygame.display.update()

def handle_movement(pink, green):
  keys_pressed = pygame.key.get_pressed()
  #Movement for pink
  if keys_pressed[pygame.K_d] and pink.x + CHAR_WIDTH <= WIDTH//2 - 20:
    pink.x += SPEED
  if keys_pressed[pygame.K_a] and pink.x >= 0:
    pink.x -= SPEED
  if keys_pressed[pygame.K_w] and pink.y >= 0:
    pink.y -= SPEED
  if keys_pressed[pygame.K_s] and pink.y + CHAR_HEIGHT <= HEIGHT:
    pink.y += SPEED

  #Movement for green
  if keys_pressed[pygame.K_RIGHT] and green.x + CHAR_WIDTH <= WIDTH:
    green.x += SPEED
  if keys_pressed[pygame.K_LEFT] and green.x >= WIDTH//2 + 20:
    green.x -= SPEED
  if keys_pressed[pygame.K_UP] and green.y >= 0:
    green.y -= SPEED
  if keys_pressed[pygame.K_DOWN] and green.y + CHAR_HEIGHT <= HEIGHT:
    green.y += SPEED



def shoot_bullets(bullets):
  for bullet in bullets:
      bullet.x += 20
      if bullet.x >= WIDTH:
        bullets.remove(bullet)


def main():
  pink = pygame.Rect(10, (HEIGHT//2)-(CHAR_HEIGHT//2), 
                     CHAR_WIDTH, CHAR_HEIGHT)
  green = pygame.Rect(WIDTH - CHAR_WIDTH - 10, 
                      (HEIGHT//2)-(CHAR_HEIGHT//2),
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
        if event.key == pygame.K_f:
          bullet = pygame.Rect(pink.x + CHAR_WIDTH, pink.y + 15, 1, 1)
          bullets.append(bullet)
          
    shoot_bullets(bullets)

    handle_movement(pink, green)

    update_display(pink, green, bullets)

  pygame.quit()

if __name__ == "__main__":
  main()
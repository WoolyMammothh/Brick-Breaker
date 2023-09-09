import pygame
import os
pygame.font.init()
pygame.mixer.init()

BLACK, WHITE = (0, 0, 0), (255, 255, 255)
WIDTH, HEIGHT = 1000, 600
CHAR_HEIGHT, CHAR_WIDTH = 70, 70
SPEED = 6
BULLET_SPEED = 12
screen = pygame.display.set_mode((WIDTH, HEIGHT))
lives_text = pygame.font.SysFont('monospace', 20, True, False)
winner_text = pygame.font.SysFont('monospace', 60, True, False)
SHOTS = pygame.mixer.Sound(os.path.join('Assets', 'shots.mp3'))
SCREAM = pygame.mixer.Sound(os.path.join('Assets', 'scream2.mp3'))
# paddle = pygame.draw.rect(screen, WHITE, (100, 50))

#HIT EVENTS
GREEN_HIT = pygame.USEREVENT + 1
PINK_HIT = pygame.USEREVENT + 2

#CHARACTERS
char1_image = pygame.image.load(os.path.join('Assets', 'character.png'))
character = pygame.transform.scale(char1_image, (CHAR_WIDTH, CHAR_HEIGHT))
char2_image = pygame.image.load(os.path.join('Assets', 'character2.png'))
charactersized = pygame.transform.scale(char2_image, (CHAR_WIDTH, CHAR_HEIGHT))
character2 = pygame.transform.flip(charactersized, True, False)
  
#BULLETS
bullet_pic = pygame.image.load(os.path.join('Assets', 'child.png'))
child = pygame.transform.scale(bullet_pic, (25, 25))
bullet2_pic = pygame.image.load(os.path.join('Assets', 'child2.png'))
childsized = pygame.transform.scale(bullet2_pic, (25, 25))
child2 = pygame.transform.flip(childsized, True, False)

#MAP
MAP = pygame.image.load(os.path.join('Assets', 'bg7.jpeg'))
MAP = pygame.transform.scale(MAP, (WIDTH, HEIGHT))

def update_display(pink, green, pink_bullets, green_bullets, pink_lives, green_lives):
  screen.fill(BLACK)
  screen.blit(MAP, (0, 0))

  pink_lives_text = lives_text.render(f'Lives: {str(pink_lives)}', 1, WHITE)
  green_lives_text = lives_text.render(f'Lives: {str(green_lives)}', 1, WHITE)

  screen.blit(character, (pink.x, pink.y))
  screen.blit(character2, (green.x, green.y))
  screen.blit(pink_lives_text, (10, 10))
  screen.blit(green_lives_text, (WIDTH - green_lives_text.get_width() - 10, 10))

  for bullet in pink_bullets:
    pygame.draw.rect(screen, BLACK, bullet)
    screen.blit(child, bullet)

  for bullet in green_bullets:
    pygame.draw.rect(screen, BLACK, bullet)
    screen.blit(child2, bullet)

  pygame.display.update()

def winner(text):
  winner = winner_text.render(text, 1, WHITE)
  screen.blit(winner, (WIDTH//2 - winner.get_width()//2, HEIGHT//2 - winner.get_height()//2))
  pygame.display.update()
  pygame.time.delay(5000)

def handle_movement(pink, green):
  keys_pressed = pygame.key.get_pressed()
  #Movement for pink
  if keys_pressed[pygame.K_d] and pink.x + CHAR_WIDTH <= WIDTH//2 - 50:
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
  if keys_pressed[pygame.K_LEFT] and green.x >= WIDTH//2 + 50:
    green.x -= SPEED
  if keys_pressed[pygame.K_UP] and green.y >= 0:
    green.y -= SPEED
  if keys_pressed[pygame.K_DOWN] and green.y + CHAR_HEIGHT <= HEIGHT:
    green.y += SPEED



def shoot_bullets(pink, green, pink_bullets, green_bullets):
  for bullet in pink_bullets:
      bullet.x += 20
      if green.colliderect(bullet):
        pygame.event.post(pygame.event.Event(GREEN_HIT))
        pink_bullets.remove(bullet)
      elif bullet.x > WIDTH:
        pink_bullets.remove(bullet)
  
  for bullet in green_bullets:
      bullet.x -= 20
      if pink.colliderect(bullet):
        pygame.event.post(pygame.event.Event(PINK_HIT))
        green_bullets.remove(bullet)
      elif bullet.x > WIDTH:
        pink_bullets.remove(bullet)



def main():
  pink = pygame.Rect(10, (HEIGHT//2)-(CHAR_HEIGHT//2), 
                     CHAR_WIDTH, CHAR_HEIGHT)
  green = pygame.Rect(WIDTH - CHAR_WIDTH - 10, 
                      (HEIGHT//2)-(CHAR_HEIGHT//2),
                      CHAR_WIDTH, CHAR_HEIGHT)
  fps = pygame.time.Clock()
  running = True
  pink_bullets = []
  green_bullets = []

  pink_lives = 10
  green_lives = 10

  winner_text = ""
  while running:
    fps.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        pygame.quit()
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_f:
          bullet = pygame.Rect(pink.x + CHAR_WIDTH, pink.y + 15, 1, 1)
          pink_bullets.append(bullet)
          SHOTS.play()

        if event.key == pygame.K_RCTRL:
          bullet = pygame.Rect(green.x, green.y + 15, 1, 1)
          green_bullets.append(bullet)
          SHOTS.play()

      if event.type == PINK_HIT:
        SCREAM.stop()
        SCREAM.play(0, 400, 1)
        pink_lives -= 1
      if event.type == GREEN_HIT:
        SCREAM.stop()
        SCREAM.play(0, 400, 1)
        green_lives -= 1
    
    winner_text = ""
    if pink_lives <= 0:
      winner_text = "GREEN WINS!"
    if green_lives <= 0:
      winner_text = "PINK WINS!"  
    if winner_text != "":
      winner(winner_text)
      SCREAM.stop()
      break
    

    shoot_bullets(pink, green, pink_bullets, green_bullets)

    handle_movement(pink, green)

    update_display(pink, green, pink_bullets, green_bullets, pink_lives, green_lives)

  main()

if __name__ == "__main__":
  main()